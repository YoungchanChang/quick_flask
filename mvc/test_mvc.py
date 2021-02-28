import os, sys
PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PARENT_DIR)
from run import create_app
import pytest
import json

def multiply_by_two(x):
    return x * 2

def test_multiply_by_two():
    assert multiply_by_two(4) == 8

@pytest.fixture
def api():
    app = create_app()
    app.config['TESTING'] = True
    api = app.test_client()
    return api

def test_ping(api):
    resp = api.get('/quick_flask/ping')
    assert b'pong' in resp.data


# def test_create_user(api):
#
#     resp = api.post(
#         '/quick_flask/sign_up',
#         data = json.dumps({
#             'user_name' : 'my_user'
#         })
#     )
#     json.loads(resp.data.decode('utf-8'))
#     # pytest.set_trace()
