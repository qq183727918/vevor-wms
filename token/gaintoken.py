# _*_ coding: UTF-8 _*_
# @Time     : 2021/1/19 11:47
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : gaintoken.py
# @Software : PyCharm
import pprint
import requests


def GainToken():
    querystring = {
        "tenantId": "admin",
        "username": "murphy",
        "password": "6088b9bde6214806b775b931b817565a",
        "grant_type": "password",
        "type": "account"
    }

    url = "http://wms.test.vevor.net/api/wms-authorization-service/controller-authLoginController/login?tenantId=admin&username=murphy&password=6088b9bde6214806b775b931b817565a&grant_type=password&type=account"

    payload = ""

    headers = {
        "Content-Type": "application/json",
        "Set-Cookie": "SESSION=NjE4MWQ2YmItNzhjMC00ZmIzLWE3ZTEtYjIzOTI4Y2VlZTg2; Path=/; HttpOnly; SameSite=Lax",
        "Authorization": "Basic Y2FjNDI1MTEtMzc4ZC00MmQ0LTk4ZWUtYjdmM2U0MDU1NjE2OjE1MGU5OTI1LWUxYzctNGZlZi05ZmQ4LWIwYzU5Mzg3ZmMzMQ=="
    }

    response = requests.post(url, data=payload, headers=headers, params=querystring)

    re = response.json()

    pprint.pprint(re)

    access_token = re['data']['access_token']

    with open('./token.txt', 'w')as f:
        f.write(access_token)


if __name__ == '__main__':
    GainToken()
