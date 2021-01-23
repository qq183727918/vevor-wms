"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/20 17:45
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : receiving_button.py
@Software  : PyCharm
"""


import pprint

from setting.wms_requests.wms_data_put import put_request


class Receiving:

    def __init__(self):
        """
        签收页面，签收按钮功能
        :return
        """

    @staticmethod
    def receiving_button():
        path = '/api/wms-inbound-orders-service/controller-overseasInboundSignOrderSign/front/sign'
        payload = ""
        querystring = {
            "ids": 2
        }
        re = put_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(re)


if __name__ == '__main__':
    wms = Receiving()
    wms.receiving_button()
