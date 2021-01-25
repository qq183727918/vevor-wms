"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/23 15:21
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : capacity_select_day.py
@Software  : PyCharm
"""

import pprint
import unittest
from setting.wms_requests.wms_data_get import get_request


class Capacity_select_day(unittest.TestCase):

    def setUp(self) -> None:
        """
        天产能查询
        :return
        """

    @staticmethod
    def test_capacity_select_day():
        path = '/api/wms-inbound-orders-service/controller-overseasInboundCapacity/front/queryCapacityListByDay'

        payload = ""

        querystring = {
            "warehouseId": 1,
            "capacityTime": "2021-01-24",
            "date": 3
        }

        response = get_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(response)

    def tearDown(self) -> None:
        pass
