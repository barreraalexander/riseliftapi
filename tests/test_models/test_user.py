from server import schemas
from fastapi.testclient import TestClient
from typing import List


from tests.fixtures.user import *
from tests.fixtures.users import *

def test_create_model(
    client: TestClient
):
    res = client.post(
        "/user",
        json = {
            "email" : f'klop@gmail.com',
            "password" : 'password123', 
            "first_name": "eggsalad"
        }
    )
    new_user = schemas.UserOut(**res.json())
    assert new_user.email ==  f"klop@gmail.com"
    assert res.status_code == 201


def test_get_model_by_id(
    authorized_client: TestClient,
    test_user: schemas.UserOut
):
  
    res = authorized_client.get(f"/user/{test_user.xid}")

    model = schemas.UserOut(**res.json())

    assert test_user.model_dump()==model.model_dump()
    assert res.status_code == 200



def test_get_all_models(
    client: TestClient,
    test_users: List[schemas.UserOut],
):
    res = client.get(f"/user")
    
    all_models: List[schemas.UserOut] = res.json()

    assert len(res.json()) == len(test_users)
    assert res.status_code==200


def test_get_all_models_full(
    authorized_client: TestClient,
    test_users,
):
    res = authorized_client.get(f"/user/fullusers")
    
    assert len(res.json()) == len(test_users)
    assert res.status_code==200

def test_update_model(
    authorized_client: TestClient,
    test_user: schemas.UserOut
):

    res = authorized_client.put(
        f"/user/{test_user.xid}",
        json= {
            "email" : f'updatedme@gmail.com',
            "password" : 'password123', 
            "first_name": "eggsalad"
        }
    )

    model = schemas.UserOut(**res.json())

    assert test_user.model_dump()!=model.model_dump()
    assert res.status_code == 200

def test_delete_model(
    authorized_client: TestClient,
    test_user: schemas.UserOut
):
    res = authorized_client.delete(f"/user/{test_user.xid}")

    assert res.status_code == 204