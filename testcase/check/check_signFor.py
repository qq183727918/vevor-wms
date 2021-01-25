"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/23 17:39
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : check_signFor.py
@Software  : PyCharm
"""

import pprint
import unittest
from setting.wms_requests.wms_json_put import put_request


class Check_shippingNumberSKU_select(unittest.TestCase):

    def test_setUp(self) -> None:
        """
        清点-拆箱
        :return
        """

    @staticmethod
    def check_shippingNumberSKU_select():
        path = '/api/wms-inbound-orders-service/controller-dischargeService/front/updateDischarge'

        payload = {
            "seaChestNo": "hgh0085"
        }

        querystring = ""

        response = put_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(response)

    def tearDown(self) -> None:
        pass
