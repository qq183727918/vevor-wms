"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/24 10:56
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : singleItem_printing.py
@Software  : PyCharm
"""

import pprint

from setting.wms_requests.wms_data_put import put_request


class SingleItem_printing:

    def __init__(self):
        """
        单品拣货打印
        :return
        """

    @staticmethod
    def singleItem_printing():
        path = '/api/wms-outbound-orders-service/controller-singleProductTaskService/front/printing'

        payload = "[133]"

        querystring = {
        }

        response = put_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(response)


if __name__ == '__main__':
    wms = SingleItem_printing()
    wms.singleItem_printing()
