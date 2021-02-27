import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
print(PARENT_DIR)
sys.path.append(PARENT_DIR)
from run import create_app
def multiply_by_two(x):
    return x * 2


def test_multiply_by_two():
    assert multiply_by_two(4) == 8

import pytest

@pytest.fixture
def api():
    app = create_app()
    app.config['TESTING'] = True
    api = app.test_client()
    return api

def test_ping(api):
    resp = api.get('/quick_flask/ping')
    assert b'pong' in resp.data