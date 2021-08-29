from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_app():
    response = client.get("/wheather/Bogota")
    assert response.status_code == 200
    assert response.json()["sys"] == {
        "type": 1,
        "id": 8582,
        "country": "CO",
        "sunrise": 1630147872,
        "sunset": 1630191852
        }

    response = client.get("/wheather/Guadalajara")
    assert response.status_code == 200
    assert response.json()["sys"] == {
        "type": 2,
        "id": 268566,
        "country": "MX",
        "sunrise": 1630154192,
        "sunset": 1630199570
        }