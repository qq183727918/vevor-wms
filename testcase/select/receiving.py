"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/20 17:49
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : receiving.py
@Software  : PyCharm
"""

import pprint

from setting.wms_requests.wms_put import put_request


class Receiving:

    def __init__(self):
        """
        预约新增，提交，时间，时间段，剩余产能
        :return
        """

    @staticmethod
    def test_receiving_button():
        path = '/wms-inbound-orders-service/controller-overseasInboundSignOrderSign/front/getList'
        payload = ""
        querystring = {
            "orderSn": "",
            "transSn": "",
            "status": "",
            "startTime": "",
            "endTime": "",
            "currentPage": 1,
            "pageSize": 10
        }
        re = put_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(re)


if __name__ == '__main__':
    wms = Receiving()
    wms.test_receiving_button()
