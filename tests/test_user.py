from server import schemas

def test_create_user(
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


# def test_get_user(
#     authorized_client,
#     test_user: schemas.UserOut
# ):
#     res = authorized_client.get(f"/user/{test_user._id}")

#     user = schemas.UserOut(**res.json())

#     assert test_user.model_dump()==user.model_dump()
#     assert res.status_code == 200



# def test_get_users(
#     client,
#     test_users,
# ):
#     res = client.get(f"/user/")
    
#     assert len(res.json()) == len(test_users)
#     assert res.status_code==200



# def test_get_usersfull(
#     authorized_client,
#     test_users,
# ):
#     res = authorized_client.get(f"/user/fullusers")
    
#     assert len(res.json()) == len(test_users)
#     assert res.status_code==200

# def test_update_user(
#     authorized_client,
#     test_user: schemas.UserOut
# ):

#     res = authorized_client.put(
#         f"/user/{test_user._id}",
#         json= {
#             "email" : f'updatedme@gmail.com',
#             "password" : 'password123', 
#             "first_name": "eggsalad"
#         }
#     )

#     user = schemas.UserOut(**res.json())

#     assert test_user.model_dump()!=user.model_dump()
#     assert res.status_code == 200


# def test_delete_user(
#     authorized_client,
#     test_user: schemas.UserOut
# ):
#     res = authorized_client.delete(f"/user/{test_user._id}")

#     assert res.status_code == 204