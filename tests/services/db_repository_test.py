from testcontainers.postgres import PostgresContainer
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from services.db.urL_service import UrlService, Url
from services.db.model import Base

@pytest.fixture
def db_session():
    container_client = PostgresContainer("postgres:16")

    with container_client:
        engine = create_engine(url=container_client.get_connection_url(), echo=True)
        session = Session(bind=engine)
        Base.metadata.create_all(engine)
        yield session
        session.close()


@pytest.fixture
def url_service(db_session):
    return UrlService(client_session=db_session)


def test_add_url(url_service, db_session):
    url_service.add_url("http://test.com", "test")

    assert db_session.query(Url).count() == 1
    assert db_session.query(Url).first().long_url == "http://test.com"
    assert db_session.query(Url).first().short_url == "test"


def test_get_original_url(url_service):
    url_service.add_url("http://test.com", "test")

    assert url_service.get_original_url("test") == "http://test.com"


def test_get_short_code(url_service):
    url_service.add_url("http://test.com", "test")

    assert url_service.get_short_code("http://test.com").short_url == "test"

def test_should_raise_exception_for_duplicate_url(url_service):
    url_service.add_url("http://test.com", "test")

    with pytest.raises(Exception):
        url_service.add_url("http://test.com", "test_new")
    
def test_should_raise_exception_for_duplicate_short_code(url_service):
    url_service.add_url("http://test.com", "test")

    with pytest.raises(Exception):
        url_service.add_url("http://test_new.com", "test")