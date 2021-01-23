"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/23 15:20
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : capacity_delete.py
@Software  : PyCharm
"""

import pprint

from setting.wms_requests.wms_data_put import put_request


class Capacity_delete:

    def __init__(self):
        """
        产能删除
        :return
        """

    @staticmethod
    def capacity_delete():
        path = '/api/wms-inbound-orders-service/controller-overseasInboundCapacity/front/deleteCapacity'
        payload = "[105]"

        querystring = ""

        response = put_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(response)


if __name__ == '__main__':
    wms = Capacity_delete()
    wms.capacity_delete()
