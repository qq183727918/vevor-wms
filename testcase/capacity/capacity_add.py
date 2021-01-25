"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/23 15:19
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : capacity_add.py
@Software  : PyCharm
"""

import pprint
import unittest
from setting.wms_requests.wms_json_post import post_request


class Capacity_add(unittest.TestCase):

    def setUp(self) -> None:
        """
        产能新增
        :return
        """

    @staticmethod
    def test_capacity_add():
        path = '/api/wms-inbound-orders-service/controller-overseasInboundCapacity/front/updateCapacity'

        payload = {
            "capacityDictKey": 17,
            "capacityTime": "2021-01-23",
            "maxNum": "152",
            "warehouseId": 1
        }

        querystring = ""

        response = post_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(response)


    def tearDown(self) -> None:
        pass

