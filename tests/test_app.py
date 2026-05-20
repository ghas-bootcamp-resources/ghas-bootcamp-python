import pickle

import pytest

from server.database import initialize_database
from server.webapp import flaskapp
import server.routes


@pytest.fixture()
def client():
    initialize_database()
    flaskapp.config["TESTING"] = True
    return flaskapp.test_client()


def test_home_page_lists_seed_books(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"PageTurner Library Admin" in response.data
    assert b"Kindred" in response.data


def test_documents_and_download(client):
    documents = client.get("/documents")
    download = client.get("/download?file=welcome.txt")

    assert documents.status_code == 200
    assert "welcome.txt" in documents.get_json()["files"]
    assert b"Welcome to PageTurner" in download.data


def test_import_session_accepts_pickled_state(client):
    response = client.post("/imports/session", data=pickle.dumps({"user": "morgan"}))

    assert response.status_code == 200
    assert response.get_json() == {"status": "imported", "keys": ["user"]}


def test_redirect_helper(client):
    response = client.get("/go?next=/documents")

    assert response.status_code == 302
    assert response.headers["Location"] == "/documents"