from app import create_app


app = create_app()
client = app.test_client()


def test_home_page():
    response = client.get("/")
    assert response.status_code == 200


def test_about_page():
    response = client.get("/about")
    assert response.status_code == 200


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {
        "status": "healthy"
    }


def test_404_page():
    response = client.get("/this-page-does-not-exist")
    assert response.status_code == 404