from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_home():
    response = client.get('/')

    assert response.json() == {'status':'ok'}
    assert response.status_code == 200