from server import schemas
from fastapi.testclient import TestClient
from typing import List

def test_create_model(
    authorized_client: TestClient,
    # test_user,
):
    res = authorized_client.post(
        "/user_demographic/",
        json= {
            "height" : 0,
            "weight" : 146, 
            "weight_goal": 0
        }
    )

    new_model = schemas.UserDemographicOut(**res.json())
    assert res.status_code == 201


def test_get_model_by_id(
    authorized_client: TestClient,
    test_user_demographic: schemas.UserDemographicOut
):
    res = authorized_client.get(f"/user_demographic/{test_user_demographic.xid}")

    model = schemas.UserDemographicOut(**res.json())
    assert res.status_code == 200

# what
def test_get_models(
    authorized_client: TestClient,
    test_user_demographic: schemas.UserDemographicOut
):
    res = authorized_client.get(f"/user_demographic")
    
    all_models: List[schemas.UserDemographicOut] = res.json()

    assert res.status_code == 200


def test_update_model(
    authorized_client: TestClient,
    test_user_demographic: schemas.UserDemographicOut
):

    res = authorized_client.put(
        f"/user_demographic/{test_user_demographic.xid}",
        json= {
            "weight" : 1000,
            "activity_level": 1
        }
    )

    model = schemas.UserDemographicOut(**res.json())

    assert test_user_demographic.model_dump()!=model.model_dump()
    assert res.status_code == 200

def test_delete_model(
    authorized_client: TestClient,
    test_user_demographic: schemas.UserDemographicOut

):
    res = authorized_client.delete(f"/user_demographic/{test_user_demographic.xid}")
    assert res.status_code == 204