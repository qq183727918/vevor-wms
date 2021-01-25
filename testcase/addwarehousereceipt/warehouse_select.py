"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/22 15:43
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : warehouse_select.py
@Software  : PyCharm
"""

import pprint
import unittest

from setting.wms_requests.wms_data_get import get_request


class Appointment(unittest.TestCase):

    def setUp(self) -> None:
        """
        入库单页面查询
        :return
        """

    def test_appointment_add(self):
        self.path = '/api/wms-inbound-orders-service/controller-overseasInboundOrderItems/front/queryInboundOrderList'
        self.payload = ""
        self.querystring = {
            "currentPage": 1,
            "pageSize": 10,
            "orderSn": "",
            "status": "",
            "chineseName": "",
            "transType": "",
            "targetWarehouse": "",
            "createdStartTime": "",
            "createdEndTime": ""
        }
        self.re = get_request(path=self.path, payload=self.payload, querystring=self.querystring)

        pprint.pprint(self.re)

    def tearDown(self) -> None:
        pass
