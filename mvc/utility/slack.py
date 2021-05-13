import traceback
import configparser
config = configparser.ConfigParser()
config.read("./log/config.ini")

import requests, json

class SendSlack(object):
    """
        Slack Income API URL을 사용 하여 메세지를 슬랙으로 보낸다.
    """

    def __init__(self, title: str, message: str):
        self._title = title
        self._message = message

        url = config["slack_income"]["url"]
        self._send = SendApiMessage(url)

    def send_message_to_slack(self):
        body = {
            "attachments": [
                {
                    "color": "#D00000",
                    "fields": [
                        {
                            "title": self._title,
                            "value": self._message,
                            "short": False
                        }
                    ]
                }
            ]
        }

        self._send.no_reponse_post_send_message(body)

class SendApiMessage(object):
    """
        외부 url api 연동 (파파고, accuweather)
    Attributes:
        url: 외부 api url 주소
    """

    def __init__(self, url=""):
        self._url = url

    @property   # getter
    def url(self):
        return self._url

    @url.setter     # setter
    def url(self, url):
        self._url = url

    def get_send_message(self, params=None, timeout=5):
        """
            Request Get 방식
        Args:
             params: 파라미터
             timeout: 시간 제한
        """
        print(" ########## get_send_message ########## ")
        ret_data = None
        get_url = self._url

        print(f" \n\t get_url: {get_url} \n")

        try:
            res = requests.get(get_url, params=params, verify=False, timeout=timeout)
            if res.status_code == 200:
                ret_data = res.json()
            else:
                res.raise_for_status()
        except Exception as e:
            print(traceback.format_exc())
            print(f"예외 발생: {e}")
            raise

        return ret_data

    def post_send_message(self, body, header=None, timeout=5):
        print(" ########## post_send_message ########## ")
        url = self._url
        ret_data = None

        print(f" \n\t url: {url} \n")
        if header is None:
            header = {
                "Content-Type": "application/json; charset=utf-8"
            }

        try:
            res = requests.post(url, data=json.dumps(body), headers=header, verify=False, timeout=timeout)

            if res.status_code == 200:
                ret_data = res.json()
            else:
                res.raise_for_status()
        except Exception as e:
            print(traceback.format_exc())
            print(f"예외 발생: {e}")
            raise

        return ret_data

    def no_reponse_post_send_message(self, body, header=None):
        url = self._url

        if header is None:
            header = {
                "Content-Type": "application/json; charset=utf-8"
            }

        try:
            res = requests.post(url, data=json.dumps(body), headers=header, verify=False, timeout=5)

            if res.status_code == 200:
                pass
            else:
                res.raise_for_status()
        except Exception as e:
            print(f"예외 발생: {e}")
            raise