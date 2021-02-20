from mvc.model import HashModel, MySQLModeling

hash_model = HashModel()

class ValueException(Exception):
    """input 값이 잘못된 값일 때 사용한다."""


class ValidateValue:
    @staticmethod
    def is_validate_data(data):
        if not isinstance(data, str):  # 데이터에 대한 검증을 하는 메소드
            raise ValueException
        return False


class UserControl:
    @staticmethod
    def is_user_signed(user_name):
        if ValidateValue.is_validate_data(user_name):  # False이면 404에러 발생
            raise ValueException
        if hash_model(user_name):
            return True  # 회원가입이 된 상태
        return False  # 회원가입이 되지 않은 상태
