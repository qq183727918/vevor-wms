"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/23 15:19
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : capacity_add.py
@Software  : PyCharm
"""

import pprint

from setting.wms_requests.wms_json_post import post_request


class Capacity_add:

    def __init__(self):
        """
        产能新增
        :return
        """

    @staticmethod
    def capacity_add():
        path = '/api/wms-inbound-orders-service/controller-overseasInboundCapacity/front/updateCapacity'

        payload = {
            "capacityDictKey": 17,
            "capacityTime": "2021-01-23",
            "maxNum": "152",
            "warehouseId": 1
        }

        querystring = ""

        response = post_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(response)


if __name__ == '__main__':
    wms = Capacity_add()
    wms.capacity_add()
