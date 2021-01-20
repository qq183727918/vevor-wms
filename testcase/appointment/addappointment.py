"""
_*_ coding: UTF-8 _*_
@Time     : 2021/1/19 19:13
@Author   : LiuXiaoQiang
@Site     : https://github.com/qq183727918
@File     : add_appointment.py
@Software : PyCharm
 """

import pprint

from setting.wms_requests.wms_post import post_request


class Appointment:

    def __init__(self):
        """
        预约新增，提交，时间，时间段，剩余产能
        :return
        """

    @staticmethod
    def test_add_appointment():
        path = '/wms-inbound-orders-service/controller-overseasInboundOrderAppointment/front/insertTime'
        payload = '[22]'
        querystring = {
            "capacityId": 12
        }
        re = post_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(re)


if __name__ == '__main__':
    wms = Appointment()
    wms.test_add_appointment()
