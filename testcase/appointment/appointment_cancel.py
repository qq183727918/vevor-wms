"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/23 14:57
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : appointment_cancel.py
@Software  : PyCharm
"""
import pprint

from setting.wms_requests.wms_json_put import put_request


class Appointment_cancel:

    def __init__(self):
        """
        预约取消
        :return
        """

    @staticmethod
    def appointment_cancel():
        path = '/api/wms-inbound-orders-service/controller-overseasInboundReservation/front/inspect'

        payload = {
            "collect": [6],
            "status": 1
        }

        querystring = ""

        response = put_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(response)


if __name__ == '__main__':
    wms = Appointment_cancel()
    wms.appointment_cancel()
