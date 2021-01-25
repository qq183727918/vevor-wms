"""
_*_ coding: UTF-8 _*_
@Time     : 2021/1/19 19:13
@Author   : LiuXiaoQiang
@Site     : https://github.com/qq183727918
@File     : appointment_add.py
@Software : PyCharm
 """

import pprint
import unittest
from setting.wms_requests.wms_data_post import post_request


class Appointment(unittest.TestCase):

    def setUp(self) -> None:
        """
        预约新增，新增提交
        :return
        """

    def test_appointment_add(self):
        self.path = '/api/wms-inbound-orders-service/controller-overseasInboundOrderAppointment/front/insertTime'
        self.payload = "[25]"
        self.querystring = {
            "capacityId": 106
        }
        re = post_request(path=self.path, payload=self.payload, querystring=self.querystring)

        pprint.pprint(re)

    def tearDown(self) -> None:
        pass
