from server import schemas

def test_create_trainer_profile(
    client
):
    res = client.post(
        "/user/",
        json= {
            "email" : f'klop@gmail.com',
            "password" : 'password123', 
            "first_name": "eggsalad"
        }
    )

    new_user = schemas.UserOut(**res.json())
    assert new_user.email ==  f"klop@gmail.com"
    assert res.status_code == 201
