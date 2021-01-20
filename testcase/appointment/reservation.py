# _*_ coding: UTF-8 _*_
# @Time     : 2021/1/19 13:25
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : reservation.py
# @Software : PyCharm

import requests
import pprint
from wmstoken.readtoken import read
from config.wms_params import test_url
from config.wms_params import responseCode_two
from wmstoken.judgmentFailure import judgmentFailure


class Reservation:

    def __init__(self):
        """
        预约新增，预约数据查询接口
        :return
        """
        self.wms_url = test_url()

    def test_reservation(self):

        url = f'{self.wms_url}/api/wms-inbound-orders-service/controller-overseasInboundOrderAppointment/front/getAddList'
        # 定义token
        token = read()
        payload = ""
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        querystring = {
            "currentPage": 1,
            "pageSize": 10
        }
        response = requests.get(url, data=payload, headers=headers, params=querystring)

        re = response.json()

        code = re['code']

        responseCode = judgmentFailure(code)

        if responseCode is not responseCode_two():
            self.test_reservation()
        else:
            pprint.pprint(re)


if __name__ == '__main__':
    wms = Reservation()
    wms.test_reservation()
