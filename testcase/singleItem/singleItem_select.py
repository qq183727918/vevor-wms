"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/24 10:51
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : singleItem_select.py
@Software  : PyCharm
"""

import pprint
import unittest
from setting.wms_requests.wms_data_get import get_request


class SingleItem_select(unittest.TestCase):

    def setUp(self) -> None:
        """
        单品拣货查询
        :return
        """

    @staticmethod
    def test_singleItem_select():
        path = '/api/wms-outbound-orders-service/controller-singleProductTaskService/front/getSingleList'

        payload = ""

        querystring = {
            "startTime": "2021-01-22 00:00:00",
            "endTime": "2021-01-24 00:00:00",
            "taskNo": "RW2021012310000001",
            "status": 0,
            "warehouseId": 2,
            "currentPage": 1,
            "pageSize": 10
        }

        response = get_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(response)

    def tearDown(self) -> None:
        pass
