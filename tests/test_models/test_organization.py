from server import schemas
from fastapi.testclient import TestClient

def test_create_organization(
    authorized_client: TestClient
):
    res = authorized_client.post(
        "/organization",
        json= {
            "name" : "Crunch Exercise Company",
            "display_name" : "Crunch!",
        }
    )

    new_organization = schemas.OrganizationOut(**res.json())
    # assert new_organization.email ==  f"klop@gmail.com"
    assert res.status_code == 201

def test_get_organization_by_id(
    authorized_client: TestClient,
    test_organization: schemas.OrganizationOut
):
  
    res = authorized_client.get(f"/organization/{test_organization.xid}")

    organization = schemas.OrganizationOut(**res.json())

    assert test_organization.model_dump()==organization.model_dump()
    assert res.status_code == 200


# def test_get_all_organizations(
#     client: TestClient,
#     test_organization: List[schemas.UserOut],
# ):
#     res = client.get(f"/user/")
    
#     assert len(res.json()) == len(test_users)
#     assert res.status_code==200



def test_update_organization(
    authorized_client: TestClient,
    test_organization: schemas.OrganizationOut
):

    res = authorized_client.put(
        f"/organization/{test_organization.xid}",
        json= {
            "display_name" : f'updated display name',
        }
    )

    organization = schemas.OrganizationOut(**res.json())

    assert test_organization.model_dump()!=organization.model_dump()
    assert res.status_code == 200
    

def test_delete_organization(
    authorized_client: TestClient,
    test_organization: schemas.OrganizationOut
):
    res = authorized_client.delete(f"/organization/{test_organization.xid}")

    assert res.status_code == 204