"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/20 16:17
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : warehouse.py
@Software  : PyCharm
"""

import pprint

from config.wms_params import debug_url
from setting.wms_requests.wms_get import Get_request


class Warehouse:

    def __init__(self):
        """
        预约新增页面，预约数据查询接口
        :return
        """

    @staticmethod
    def test_select_warehouse():
        path = '/wms-inbound-orders-service/controller-overseasInboundOrderAppointment/front/getAddList'
        querystring = {
            "currentPage": 1,
            "pageSize": 10
        }
        payload = ""

        re = Get_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(re)


if __name__ == '__main__':
    wms = Warehouse()
    wms.test_select_warehouse()
