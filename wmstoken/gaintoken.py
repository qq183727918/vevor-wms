# _*_ coding: UTF-8 _*_
# @Time     : 2021/1/19 11:47
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : gaintoken.py
# @Software : PyCharm
import pprint

import requests

from config.wms_params import test_url


class GainToken:
    def __init__(self):
        """
        刷新token
        """
        self.wms = test_url()

    def gainToken(self):
        querystring = {
            "tenantId": "admin",
            "username": "murphy",
            "password": "6088b9bde6214806b775b931b817565a",
            "grant_type": "password",
            "type": "account"
        }

        url = f"{self.wms}/api/wms-authorization-service/controller-authLoginController/login?tenantId=admin&username=murphy&password=6088b9bde6214806b775b931b817565a&grant_type=password&type=account"

        payload = ""

        headers = {
            "Content-Type": "application/json",
            "Set-Cookie": "SESSION=NTBjZTRkNGItYjk5Yy00MmYxLWE2N2MtMTAwNTE3YzFlYjkw; Path=/; HttpOnly; SameSite=Lax",
            "Authorization": "Basic Y2FjNDI1MTEtMzc4ZC00MmQ0LTk4ZWUtYjdmM2U0MDU1NjE2OjE1MGU5OTI1LWUxYzctNGZlZi05ZmQ4LWIwYzU5Mzg3ZmMzMQ==",
            "Cookie": "SESSION=ODgxOTM4MjgtMThjYi00ZjkyLTgyNjUtOWM1YmI2MGRhNmJl; isSupperTenant=true; expiresIn=3530606; requestTime=1611455726511",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
        }

        response = requests.post(url, json=payload, headers=headers, params=querystring, verify=False)

        re = response.json()

        pprint.pprint(re)

        access_token = re['data']['access_token']

        code = re['code']

        with open(r'D:\Tools\vevor\vevor-wms\wmstoken\token.txt', 'w')as f:
            f.write(access_token)

        return code


if __name__ == '__main__':
    wms = GainToken()
    wms.gainToken()
