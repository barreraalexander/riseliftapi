from server import schemas
from fastapi.testclient import TestClient
from typing import List

def test_create_model(
    authorized_client: TestClient
):
    res = authorized_client.post(
        "/organization",
        json= {
            "name" : "Crunch Exercise Company",
            "display_name" : "Crunch!",
        }
    )

    new_model = schemas.OrganizationOut(**res.json())
    
    assert res.status_code == 201

def test_get_model_by_id(
    authorized_client: TestClient,
    test_organization: schemas.OrganizationOut
):
  
    res = authorized_client.get(f"/organization/{test_organization.xid}")

    new_model = schemas.OrganizationOut(**res.json())

    assert test_organization.model_dump()==new_model.model_dump()
    assert res.status_code == 200


def test_get_all_models(
    client: TestClient,
    test_organization: schemas.OrganizationOut,
):
    res = client.get(f"/organization")
    
    assert res.status_code==200



def test_update_model(
    authorized_client: TestClient,
    test_organization: schemas.OrganizationOut
):

    res = authorized_client.put(
        f"/organization/{test_organization.xid}",
        json= {
            "display_name" : f'updated display name',
        }
    )

    model = schemas.OrganizationOut(**res.json())

    assert test_organization.model_dump()!=model.model_dump()
    assert res.status_code == 200
    

def test_delete_model(
    authorized_client: TestClient,
    test_organization: schemas.OrganizationOut
):
    res = authorized_client.delete(f"/organization/{test_organization.xid}")

    assert res.status_code == 204