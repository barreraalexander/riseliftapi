from server import schemas
from fastapi.testclient import TestClient
from typing import List

def test_create_exercise(
    authorized_client: TestClient
):
    res = authorized_client.post(
        "/exercise",
        json= {
            "name" : 'crunches',
        }
    )

    # new_model = schemas.ExerciseOut(**res.json())
    assert res.status_code == 201


