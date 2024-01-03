from server import schemas
from fastapi.testclient import TestClient

def test_create_trainer_profile(
    authorized_client: TestClient,
    test_organization: schemas.OrganizationOut,
):
    res = authorized_client.post(
        "/trainer_profile",
        json = {
            "override_display_name" : 'Chaz Bundick',
            "organization_xid" : test_organization.xid
        }
    )

    new_schema = schemas.TrainerProfileOut(**res.json())

    assert res.status_code == 201


def test_get_trainer_profile(
    authorized_client: TestClient,
    test_trainer_profile: schemas.TrainerProfileOut
):
  
    res = authorized_client.get(f"/trainer_profile/{test_trainer_profile.xid}")

    trainer_profile = schemas.TrainerProfileOut(**res.json())

    assert test_trainer_profile.model_dump()==trainer_profile.model_dump()
    assert res.status_code == 200


def test_update_trainer_profile(
    authorized_client: TestClient,
    test_trainer_profile: schemas.TrainerProfileOut
):

    res = authorized_client.put(
        f"/trainer_profile/{test_trainer_profile.xid}",
        json= {
            "override_display_name" : 'updated overridden display name',
        }
    )

    print (res.json())

    trainer_profile = schemas.TrainerProfileOut(**res.json())

    # assert test_trainer_profile.model_dump()!=trainer_profile.model_dump()
    # assert res.status_code == 200