import pytest
from server import models, schemas

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