"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/23 15:12
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : appointment_detail.py
@Software  : PyCharm
"""

import pprint
import unittest
from setting.wms_requests.wms_data_get import get_request


class Appointment_detail(unittest.TestCase):

    def setUp(self) -> None:
        """
        预约详情页面
        :return
        """

    @staticmethod
    def test_appointment_detail():
        path = '/api/wms-inbound-orders-service/controller-overseasInboundOrderAppointment/front/getUpdateList'

        payload = ""

        querystring = {
            "currentPage": 1,
            "pageSize": 10,
            "id": 8
        }

        response = get_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(response)

    def tearDown(self) -> None:
        pass
