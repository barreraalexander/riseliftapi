import pytest
from server import create_app, schemas, models
from server.settings import settings
from server.database import Base, get_db
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from server.oauth2 import create_access_token



app = create_app()
client = TestClient(app)

DATABASE_URL = f'mysql+pymysql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(DATABASE_URL)


TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


@pytest.fixture()
def session():

    # Base.metadata.drop_all(bind=engine, tables=[models.TrainerProfile.__table__])

    # Base.metadata.delete
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app = create_app()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)









@pytest.fixture
def test_user_demographic(
    authorized_client: TestClient,
):
    user_demographic_data = {
        "height" : 0,
        "weight" : 146, 
        "weight_goal": 0
    }

    res = authorized_client.post(
        "/user_demographic/",
        json=user_demographic_data
    )

    assert res.status_code == 201

    new_user_demographic = res.json()
    return schemas.UserDemographicOut(**new_user_demographic)


@pytest.fixture
def test_organization(
    authorized_client: TestClient,
):
    organization_data = {
        "name" : "Dojo Golbez",
        "display_name" : "! Dojo Golbez !"
    }

    res = authorized_client.post(
        "/organization",
        json=organization_data
    )

    assert res.status_code == 201

    new_organization = res.json()
    return schemas.OrganizationOut(**new_organization)


@pytest.fixture
def test_trainer_profile(
    authorized_client: TestClient,
    test_organization: schemas.OrganizationOut
):
    trainer_profile_data = {
        "override_display_name" : "The Raptor",
        "organization_xid" : test_organization.xid
    }

    res = authorized_client.post(
        "/trainer_profile",
        json=trainer_profile_data
    )

    assert res.status_code == 201

    new_trainer_proflie = res.json()
    return schemas.TrainerProfileOut(**new_trainer_proflie)


@pytest.fixture
def token(test_user):
    return create_access_token({
        "xid" : test_user.xid,
    })

@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }

    return client