
def test_test():
    assert 2 == 2



from fastapi.testclient import TestClient
from .conftest import app


#client = TestClient(app)

client = TestClient()



def test_create_movie():
    response = client.post(
        "/API/movies",
        json={"title": "deadpool@example.com", "description": "chimichangas4life"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
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




# get all movies
def test_get_all_movies(add_movie):
    with TestClient(app) as client:
        # given
        movie_one = add_movie('nico','desc1')
        movie_two = add_movie('algo','desc2')

        # when
        response = client.get("/API/movies/")
        data = response.json()

        # then
        assert response.status_code == 200
        assert data[0]['title'] == movie_one['title']
        assert data[1]['title'] == movie_two['title']
        assert data[1]['description'] == movie_two['description']
        assert len(data) == 2






#pytest --capture=no