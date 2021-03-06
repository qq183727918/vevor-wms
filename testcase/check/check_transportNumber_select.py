"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/23 16:18
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : check_transportNumber_select.py
@Software  : PyCharm
"""

import pprint
import unittest
from setting.wms_requests.wms_data_get import get_request


class Check_transportNumber_select(unittest.TestCase):

    def setUp(self) -> None:
        """
        清点查询-运输号信息
        :return
        """

    @staticmethod
    def test_check_transportNumber_select():
        path = '/api/wms-inbound-orders-service/controller-dischargeService/front/getDischargeTop'

        payload = ""

        querystring = {
            "currentPage": 1,
            "pageSize": 10,
            "seaChestNo": "HGH0085"
        }

        response = get_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(response)

    def tearDown(self) -> None:
        pass
