"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/24 10:48
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : pickingTable_select.py
@Software  : PyCharm
"""

import pprint
import unittest
from setting.wms_requests.wms_data_get import get_request


class PickingTable_select(unittest.TestCase):

    def setUp(self) -> None:
        """
        拣货任务报表查询
        :return
        """

    @staticmethod
    def test_pickingTable_select():
        path = '/api/wms-outbound-orders-service/controller-overseasOutboundPickingTask/front/queryAll'

        payload = ""

        querystring = {
            "startTime": "2021-01-21 00:00:00",
            "endTime": "2021-01-23 00:00:00",
            "status": 0,
            "orderSn": "CK2021012200000010",
            "wareHouse": 2,
            "taskNo": "RW2021012210000003",
            "currentPage": 1,
            "pageSize": 10
        }

        response = get_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(response)


if __name__ == '__main__':
    wms = PickingTable_select()
    wms.pickingTable_select()

