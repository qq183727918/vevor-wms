"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/20 16:17
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : appointment_add_select.py
@Software  : PyCharm
"""

import pprint

from setting.wms_requests.wms_data_get import get_request


class Appointment:

    def __init__(self):
        """
        预约新增页面，预约数据查询接口
        :return
        """

    @staticmethod
    def appointment_add_select():
        path = '/api/wms-inbound-orders-service/controller-overseasInboundOrderAppointment/front/getAddList'
        querystring = {
            "startTime": "",
            "endTime": "",
            "targetWarehouse": "",
            "seaChestNo": "",
            "customerName": "",
            "orderSn": "",
            "status": "",
            "currentPage": 1,
            "pageSize": 10
        }
        payload = ""

        re = get_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(re)


if __name__ == '__main__':
    wms = Appointment()
    wms.appointment_add_select()
