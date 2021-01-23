"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/23 16:42
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : wms_json_put.py
@Software  : PyCharm
"""


import requests

from setting.config.config import wms_config
from setting.config.config import wms_headers


def put_request(path, payload, querystring):
    # 地址URL
    wms_url = wms_config()

    # URL拼接
    url = wms_url + path

    # print(url)
    # 请求头
    head = wms_headers()

    # 发送请求
    response = requests.put(url, json=payload, headers=head, params=querystring, verify=False)

    re = response.json()

    # pprint.pprint(re)

    return re
