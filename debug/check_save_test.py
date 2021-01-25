"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/23 16:37
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : check_save.py
@Software  : PyCharm
"""

import pprint
import unittest

from setting.wms_requests.wms_json_put import put_request


class Check_save(unittest.TestCase):

    def setUp(self) -> None:
        """
        清点-保存
        :return
        """

    def test_check_save(self):
        path = '/api/wms-inbound-orders-service/controller-dischargeService/front/dischargeSave'

        payload = {
            "detailList": [{
                "$index": 0,
                "finishNum": 0,
                "goodsName": "线束 97-02 1013汽车",
                "goodsSku": "97-02-1013QCXS001V0",
                "id": 47,
                "num": 8,
                "orderSn": "RK2021012000000021",
                "status": 2,
                "statusName": "待提交"
            }],
            "orderSeaChestId": 20,
            "seaChestNo": "HGH0085"
        }

        querystring = ""

        response = put_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(response)

    def tearDown(self) -> None:
        pass
