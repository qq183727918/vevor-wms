"""
_*_ coding: UTF-8 _*_
@Time     : 2021/1/19 19:13
@Author   : LiuXiaoQiang
@Site     : https://github.com/qq183727918
@File     : appointment_add.py
@Software : PyCharm
 """

import pprint

from setting.wms_requests.wms_data_post import post_request


class Appointment:

    def __init__(self):
        """
        预约新增，新增提交
        :return
        """

    @staticmethod
    def appointment_add():
        path = '/api/wms-inbound-orders-service/controller-overseasInboundOrderAppointment/front/insertTime'
        payload = "[25]"
        querystring = {
            "capacityId": 106
        }
        re = post_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(re)


if __name__ == '__main__':
    wms = Appointment()
    wms.appointment_add()
