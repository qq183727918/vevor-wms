"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/24 10:56
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : singleItem_printing.py
@Software  : PyCharm
"""

import pprint
import unittest
from setting.wms_requests.wms_data_put import put_request


class SingleItem_printing(unittest.TestCase):

    def setUp(self) -> None:
        """
        单品拣货打印
        :return
        """

    @staticmethod
    def test_singleItem_printing():
        path = '/api/wms-outbound-orders-service/controller-singleProductTaskService/front/printing'

        payload = "[133]"

        querystring = {
        }

        response = put_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(response)

    def tearDown(self) -> None:
        pass
