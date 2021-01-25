"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/23 16:15
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : receiving_select.py
@Software  : PyCharm
"""

import pprint
import unittest
from setting.wms_requests.wms_data_get import get_request


class Receiving_select(unittest.TestCase):

    def setUp(self) -> None:
        """
        签收页面，查询
        :return
        """

    @staticmethod
    def test_receiving_select():
        path = '/api/wms-inbound-orders-service/controller-overseasInboundSignOrderSign/front/getList'
        payload = ""
        querystring = {
            "startTime": "",
            "endTime": "",
            "orderSn": "",
            "targetWarehouse": "",
            "status": "",
            "transType": "",
            "transSn": "",
            "currentPage": 1,
            "pageSize": 10
        }
        re = get_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(re)

    def tearDown(self) -> None:
        pass
