"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/23 15:22
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : capacity_select_month.py
@Software  : PyCharm
"""
import pprint

from setting.wms_requests.wms_data_get import get_request


class Capacity_select_month:

    def __init__(self):
        """
        月产能查询
        :return
        """

    @staticmethod
    def capacity_select_month():
        path = '/api/wms-inbound-orders-service/controller-overseasInboundCapacity/front/queryCapacityListByDay'

        payload = ""

        querystring = {
            "warehouseId": 1,
            "capacityTime": "2021-01-24",
            "date": 1
        }

        response = get_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(response)


if __name__ == '__main__':
    wms = Capacity_select_month()
    wms.capacity_select_month()
