import pymysql

def HashModel():
    voted = {}
    def check_voter(name):
        nonlocal voted
        # db에 값이 있을 때 - 돌려보내기
        if voted.get(name):
            print("회원가입이 되어있습니다.")
            print(voted)
            return False

        # db에 값이 없을 때 - 저장한다.
        else:
            voted[name] = True
            print("회원가입을 진행했습니다.")
            return True
    return check_voter

class MySQLModeling:

    @staticmethod
    def conn_mysqldb():
        MYSQL_HOST = 'localhost'
        MYSQL_CONN = pymysql.connect(
            host=MYSQL_HOST,
            port=3306,
            user='root',
            passwd='1234',
            db='miniter',
            charset='utf8'
        )
        if not MYSQL_CONN.open:
            MYSQL_CONN.ping(reconnect=True)
        return MYSQL_CONN