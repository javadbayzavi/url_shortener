from fastapi.testclient import TestClient
from api.api import create_app
from api import url_shortener_route
import pytest


class FakeShortener:
    async def shorten_url(self, url: str) -> str:
        return "google"



class FakeExpander:
    def expand(self, url_code: str) -> str | None:
        return "https://google.com"


@pytest.fixture
def client():
    app = create_app()
    app.dependency_overrides[url_shortener_route.get_url_shortener] = lambda: FakeShortener()
    app.dependency_overrides[url_shortener_route.get_url_expander] = lambda: FakeExpander()
    client = TestClient(app)
    
    yield client

    app.dependency_overrides.clear()





def test_get_root(client):
    response = client.get("/")

    assert response.status_code == 200


def test_shorten_url(client):
    response = client.post("/urls/shorten", json={"url": "https://google.com"})

    assert response.status_code == 200
    assert response.json() == {"code": "google"}


def test_expand_url_redirect_by_default(client):
    response = client.get("/urls/expand/google", follow_redirects=False)

    assert response.status_code == 302
    assert response.headers["location"] == "https://google.com" 

def test_expand_url_without_redirect(client):
    response = client.get("/urls/expand/google?redirect=false")

    assert response.status_code == 200
    assert response.json() == {"url": "https://google.com"}