"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/23 14:57
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : appointment_cancel.py
@Software  : PyCharm
"""
import pprint
import unittest
from setting.wms_requests.wms_json_put import put_request


class Appointment_cancel(unittest.TestCase):

    def setUp(self) -> None:
        """
        预约取消
        :return
        """

    @staticmethod
    def test_appointment_cancel():
        path = '/api/wms-inbound-orders-service/controller-overseasInboundReservation/front/inspect'

        payload = {
            "collect": [6],
            "status": 1
        }

        querystring = ""

        response = put_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(response)

    def tearDown(self) -> None:
        pass
