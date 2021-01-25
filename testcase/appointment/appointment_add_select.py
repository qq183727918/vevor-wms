"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/20 16:17
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : appointment_add_select.py
@Software  : PyCharm
"""

import pprint
import unittest
from setting.wms_requests.wms_data_get import get_request


class Appointment(unittest.TestCase):

    def setUp(self) -> None:
        """
        预约新增页面，预约数据查询接口
        :return
        """

    @staticmethod
    def test_appointment_add_select():
        path = '/api/wms-inbound-orders-service/controller-overseasInboundOrderAppointment/front/getAddList'
        querystring = {
            "startTime": "",
            "endTime": "",
            "targetWarehouse": "",
            "seaChestNo": "",
            "customerName": "",
            "orderSn": "",
            "status": "",
            "currentPage": 1,
            "pageSize": 10
        }
        payload = ""

        re = get_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(re)


    def tearDown(self) -> None:
        pass
