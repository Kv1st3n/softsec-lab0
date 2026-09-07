import pytest
from flask import Flask
from src.api import app as flask_app
from src.calculator import *
import json

@pytest.fixture()
def app():
    flask_app.config.update({
        "TESTING":True,
    })
    
    yield flask_app

@pytest.fixture()
def client(app):
    return app.test_client()


def test_hello(client):
    response = client.get("/hello")
    
    assert response.status_code == 200
    assert response.get_json() == "Hello"
    

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_calc(client):
    
    data = {
        "expression": "2+3*4"
    }
    
    response = client.post(
        "/calc",
        json=data
    )
    
    json_data = response.get_json()
    assert json_data["result"] == "14"