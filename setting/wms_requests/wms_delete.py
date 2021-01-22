# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/19 20:26
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : lxq_delete.py
# @Software : PyCharm

import pprint

import requests

from setting.config.config import wms_config
from setting.config.config import wms_headers


def delete_request(path, payload, querystring):
    # 地址URL
    wms_url = wms_config()

    # URL拼接
    url = wms_url + path

    # print(url)
    # 请求头
    head = wms_headers()

    # 发送请求
    response = requests.delete(url, data=payload, headers=head, params=querystring, verify=False)

    re = response.json()

    pprint.pprint(re)

    return re
