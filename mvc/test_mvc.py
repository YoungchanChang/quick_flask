

def multiply_by_two(x):
    return x * 2


def test_multiply_by_two():
    assert multiply_by_two(4) == 7

import pytest
@pytest.fixture
def api():
    app = create_app(config.test_config)
    app.config['TESTING'] = True
    api = app.test_client()

    return api