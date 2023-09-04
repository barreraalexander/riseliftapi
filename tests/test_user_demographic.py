from server import schemas
from typing import List

def test_create_user_demographic(
    authorized_client,
    test_user,
):
    res = authorized_client.post(
        "/user_demographic/",
        json= {
            "height" : 0,
            "weight" : 146, 
            "weight_goal": 0
        }
    )

    new_user_demographic = schemas.UserDemographicOut(**res.json())
    assert res.status_code == 201


def test_get_user_demographic(
    authorized_client,
    test_user_demographic: schemas.UserDemographicOut
):
    res = authorized_client.get(f"/user_demographic/{test_user_demographic.user_demographic_id}")

    user_demographic = schemas.UserDemographicOut(**res.json())
    # assert test_user.model_dump()==user.model_dump()
    assert res.status_code == 200

def test_get_user_demographics(
    authorized_client,
    test_user_demographic: schemas.UserDemographicOut
):
    res = authorized_client.get(f"/user_demographic/")

    user_demographics: List[schemas.UserDemographicOut] = res.json()

    assert res.status_code == 200


def test_update_user_demographic(
    authorized_client,
    test_user_demographic: schemas.UserDemographicOut
):

    res = authorized_client.put(
        f"/user_demographic/{test_user_demographic.user_demographic_id}",
        json= {
            "weight" : 1000,
            "activity_level": 1
        }
    )

    user_demographic = schemas.UserDemographicOut(**res.json())

    assert test_user_demographic.model_dump()!=user_demographic.model_dump()
    assert res.status_code == 200

def test_delete_user_demographic(
    authorized_client,
    test_user_demographic: schemas.UserDemographicOut

):
    res = authorized_client.delete(f"/user_demographic/{test_user_demographic.user_demographic_id}")
    assert res.status_code == 204