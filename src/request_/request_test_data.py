import requests
import urllib3
from src.html.fu import FuHtml
from src.html.empty import EmptyHtml

class MyRequest:
    def __init__(self):
        urllib3.disable_warnings()
        self.session = requests.session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        }

    def get(self, url: str):
        """get请求

                Args:
                    url (str): 目标url

                Returns:
                    _type_: 响应内容
                """

        return FuHtml()

    def post(self, url: str, params: dict):
        """post请求

        Args:
            url (str): 目标url
            params (dict): 请求参数

        Returns:
            _type_: 响应内容
        """
        r = self.session.post(url, data=params, verify=False)
        if r.status_code != 200:
            return False
        return r.text


_my_request = MyRequest()
request_post = _my_request.post
request_get_test = _my_request.get
