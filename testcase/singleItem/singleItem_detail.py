"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/24 10:58
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : singleItem_detail.py
@Software  : PyCharm
"""

import pprint
import unittest
from setting.wms_requests.wms_data_get import get_request


class SingleItem_detail(unittest.TestCase):

    def setUp(self) -> None:
        """
        单品拣货详情
        :return
        """

    @staticmethod
    def test_singleItem_detail():
        path = '/api/wms-outbound-orders-service/controller-singleProductTaskService/front/getTaskPickDetail'

        payload = ""

        querystring = {
            "taskId": 133
        }

        response = get_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(response)

    def tearDown(self) -> None:
        pass
