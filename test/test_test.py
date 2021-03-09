import os, sys
CURRENT_DIR = (os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CURRENT_DIR)
PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PARENT_DIR)
import pytest


class Cal(object):
    def add_num_and_double(self, x, y):
        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        result *= 2
        return result


    def save(self, dir_path, file_name):
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, 'w') as f:
            f.write('test')

cal = Cal()
cal.save(CURRENT_DIR, 'test.txt')

def test_add_num_and_double():
    cal = Cal()
    assert cal.add_num_and_double(1, 1) == 4



is_release = True


class TestCal(object):



    def test_add_num_and_doubles(self, tmpdir):
        print(tmpdir)
        print("What")
        assert self.cal.add_num_and_double(1, 1) == 4

    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = Cal()
        cls.test_file_name = 'test.txt'

    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path) is True
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

    def test_add_num_and_double(self, request):
        os_name = request.config.getoption('--os-name')
        print(os_name)
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')
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
