"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/22 15:43
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : warehouse_select.py
@Software  : PyCharm
"""

import pprint

from setting.wms_requests.wms_data_get import get_request


class Appointment:

    def __init__(self):
        """
        入库单页面查询
        :return
        """

    @staticmethod
    def appointment_add():
        path = '/api/wms-inbound-orders-service/controller-overseasInboundOrderItems/front/queryInboundOrderList'
        payload = ""
        querystring = {
            "currentPage": 1,
            "pageSize": 10,
            "orderSn": "",
            "status": "",
            "chineseName": "",
            "transType": "",
            "targetWarehouse": "",
            "createdStartTime": "",
            "createdEndTime": ""
        }
        re = get_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(re)


if __name__ == '__main__':
    wms = Appointment()
    wms.appointment_add()
