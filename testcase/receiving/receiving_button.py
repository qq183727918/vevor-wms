"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/20 17:45
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : receiving_button.py
@Software  : PyCharm
"""


import pprint
import unittest
from setting.wms_requests.wms_data_put import put_request


class Receiving(unittest.TestCase):

    def setUp(self) -> None:
        """
        签收页面，签收按钮功能
        :return
        """

    @staticmethod
    def test_receiving_button():
        path = '/api/wms-inbound-orders-service/controller-overseasInboundSignOrderSign/front/sign'
        payload = ""
        querystring = {
            "ids": 2
        }
        re = put_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(re)

    def tearDown(self) -> None:
        pass
