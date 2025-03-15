from backend.tests.conf import client

def test_create_user(client): # type: ignore
    data = {"email": "ping@gmail.com", "password": "password"}
    response = client.post("/user/", json=data)
    assert response.status_code == 201
    assert response.json()["email"] == data["email"]