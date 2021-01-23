"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/23 16:38
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : check_submit.py
@Software  : PyCharm
"""

import pprint

from setting.wms_requests.wms_data_get import get_request


class Check_shippingNumberSKU_select:

    def __init__(self):
        """
        清点-提交
        :return
        """

    @staticmethod
    def check_shippingNumberSKU_select():
        path = '/api/wms-inbound-orders-service/controller-dischargeService/front/getDischargeList'

        payload = ""

        querystring = {
            "currentPage": 1,
            "pageSize": 10,
            "seaChestNo": "HGH0085"
        }

        response = get_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(response)


if __name__ == '__main__':
    wms = Check_shippingNumberSKU_select()
    wms.check_shippingNumberSKU_select()
