import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_post():
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data


def test_create_post():
    payload = {
        "title": "title",
        "body": "body",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code == 201

    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert "id" in data


def test_update_post():
    payload = {
        "id": 1,
        "title": "title1",
        "body": "body1",
        "userId": 1
    }

    response = requests.put(f"{BASE_URL}/posts/1", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert data["title"] == "title1"