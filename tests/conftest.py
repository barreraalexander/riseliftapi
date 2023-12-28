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
def test_user(
    client
):
    user_data = {
        "email" : "alicia1@gmail.com",
        "password" : "password234",
        "first_name": "Alicia"
    }

    res = client.post("/user/", json=user_data)

    assert res.status_code == 201

    new_user = res.json()
    new_user['password'] = user_data['password']
    return schemas.UserOut(**new_user)


@pytest.fixture
def test_users(
    session
):
    users_data = [
        {
            "email" : "alicia@gmail.com",
            "password" : "password234",
            "first_name": "Alicia"
        },
    
        {
            "email" : "alex@gmail.com",
            "password" : "password234",
            "first_name": "Alex"
        },
        
    ]

    def create_user_model(user):
        return models.User(**user)

    users_map = map(create_user_model, users_data)

    users = list(users_map)

    session.add_all(users)

    session.commit()

    users = session.query(models.User).all()

    return users


@pytest.fixture
def test_user_demographic(
    authorized_client,
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
def token(test_user):
    return create_access_token({
        "_id" : test_user._id,
    })

@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }

    return client