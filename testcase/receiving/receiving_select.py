"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/23 16:15
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : receiving_select.py
@Software  : PyCharm
"""

import pprint

from setting.wms_requests.wms_data_get import get_request


class Receiving_select:

    def __init__(self):
        """
        签收页面，查询
        :return
        """

    @staticmethod
    def receiving_select():
        path = '/api/wms-inbound-orders-service/controller-overseasInboundSignOrderSign/front/getList'
        payload = ""
        querystring = {
            "startTime": "",
            "endTime": "",
            "orderSn": "",
            "targetWarehouse": "",
            "status": "",
            "transType": "",
            "transSn": "",
            "currentPage": 1,
            "pageSize": 10
        }
        re = get_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(re)


if __name__ == '__main__':
    wms = Receiving_select()
    wms.receiving_select()
