# -*- coding: utf-8 -*-
import os, sys
from dotenv import load_dotenv

load_dotenv(verbose=True)

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__)))))

import pymysql
from datetime import datetime


class ConnectionUseful:

    def __init__(self):
        self._conn = get_conn()

    def get_conn(self):
        MYSQL_CONN = pymysql.connect(
            host=os.getenv('host'),
            port=int(os.getenv('port')),
            user=os.getenv('user'),
            passwd=os.getenv('passwd'),
            db='useful_elastic',
            charset=os.getenv('charset')
        )
        if not MYSQL_CONN.open:
            MYSQL_CONN.ping(reconnect=True)
        return MYSQL_CONN

    def save_server_errors(self, _svc_name, _input_json, _error_msg):
        table_name = "SERVER_ERROR_LOGc"
        conn = self._conn
        with conn.cursor() as cursor:
            sql = "INSERT INTO " + table_name + " (SVC_NAME, INPUT_JSON, MSG, TIME) VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, (_svc_name, str(_input_json), str(_error_msg), time))
            conn.commit()
        conn.close()

    def save_server_logs(self, _svc_name, _input_json, _error_msg):
        table_name = "SERVER_LOG"
        conn = self._conn
        with conn.cursor() as cursor:
            sql = "INSERT INTO " + table_name + " (SVC_NAME, INPUT_JSON, MSG, TIME) VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, (_svc_name, str(_input_json), str(_error_msg), time))
            conn.commit()
        conn.close()
