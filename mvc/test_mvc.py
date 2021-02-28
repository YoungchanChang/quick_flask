import os, sys
PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PARENT_DIR)
from run import create_app
import pytest
import json


class Cal(object):
    def add_num_and_double(self, x, y):
        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        result *= 2
        return result

def test_add_num_and_double():
    cal = Cal()
    assert cal.add_num_and_double(1, 1) == 4

is_release = True

class TestCal(object):

    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = Cal()

    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal

    def setup_method(self, method):
        """테스트 실행 동안 사용될 인스턴스 변수들을 지정해줌"""
        print('method_setup={}'.format(method.__name__))
        # self.cal = Cal()


    def teardown_method(self, method):
        """테스트 실행 동안 사용된 인스턴스 변수들을 지정해줌"""
        print('method_teardown={}'.format(method.__name__))
        # del self.cal

    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 1) == 4

    @pytest.mark.skip(reason='skip!')
    def test_add_num_and_raise(self):
        print('예외처리')
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')

    @pytest.mark.skipif(is_release==True, reason='skip!')
    def test_add_num_and_raise_if(self):
        print('예외처리')
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')


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
