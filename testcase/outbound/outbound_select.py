"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/24 10:23
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : outbound_select.py
@Software  : PyCharm
"""

import pprint

from setting.wms_requests.wms_data_get import get_request


class Outbound_select:

    def __init__(self):
        """
        出库单查询
        :return
        """

    @staticmethod
    def outbound_select():
        path = '/api/wms-outbound-orders-service/controller-overseasOutboundOrder/front/queryOutboundOrderList'

        payload = ""

        querystring = {
            "createdStartTime": "2021-01-21 00:00:00",
            "createdEndTime": "2021-01-23 00:00:00",
            "orderSn": "CK2021012200000010",
            "warehouse": 2,
            "status": 0,
            "currentPage": 1,
            "pageSize": 10
        }

        response = get_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(response)


if __name__ == '__main__':
    wms = Outbound_select()
    wms.outbound_select()
