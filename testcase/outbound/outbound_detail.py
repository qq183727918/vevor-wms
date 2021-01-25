"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/24 10:45
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : outbound_detail.py
@Software  : PyCharm
"""

import pprint
import unittest
from setting.wms_requests.wms_data_get import get_request


class Outbound_detail(unittest.TestCase):

    def setUp(self) -> None:
        """
        出库单详情
        :return
        """

    @staticmethod
    def test_outbound_detail():
        path = '/api/wms-outbound-orders-service/controller-overseasOutboundOrder/front/queryOutboundOrderById'

        payload = ""

        querystring = {
            "outboundOrderId": 161
        }

        response = get_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(response)

    def tearDown(self) -> None:
        pass
