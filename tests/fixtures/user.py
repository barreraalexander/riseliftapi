import pytest
from server import schemas

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