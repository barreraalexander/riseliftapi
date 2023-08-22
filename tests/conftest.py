import pytest
from server import create_app
from fastapi.testclient import TestClient

app = create_app()
client = TestClient(app)

@pytest.fixture()
def session():
    pass
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)
    # db = TestingSessionLocal()

@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()


    app = create_app()
    # app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


