
def test_test():
    assert 2 == 2



from fastapi.testclient import TestClient
from .conftest import app


client = TestClient(app)



def test_create_movie():
    print('dsfds')
    response = client.post(
        "/API/movies",
        json={"title": "deadpool@example.com", "description": "chimichangas4life"},
    )
    print(response)
    assert response.status_code == 200, response.text
    data = response.json()
    print(data)
    assert data["title"] == "deadpool@example.com"
    assert "id" in data
    movie_id = data["id"]

    """
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "deadpool@example.com"
    assert data["id"] == user_id
    """




#pytest --capture=no