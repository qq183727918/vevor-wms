"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/23 17:39
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : check_abnormal.py
@Software  : PyCharm
"""
import pprint
import unittest
from setting.wms_requests.wms_json_post import post_request


class Check_shippingNumberSKU_select(unittest.TestCase):

    def setUp(self) -> None:
        """
        清点-异常-确定
        :return
        """

    @staticmethod
    def test_check_shippingNumberSKU_select():
        path = '/api/wms-inbound-orders-service/controller-dischargeService/front/unusualAndSubmit'

        payload = {
            "detailList": [{
                "$index": 1,
                "finishNum": "1",
                "goodsName": "气动脚踏式液压泵",
                "goodsSku": "QDJTSYYB000000001V0",
                "id": 46,
                "num": 2,
                "orderSn": "RK2021012000000021",
                "status": 2,
                "statusName": "待提交",
            }],
            "orderSeaChestId": 20,
            "seaChestNo": "HGH0085",
            "unusualList": [{
                "attachmentId": "",
                "fileList": [],
                "goodsSku": "QDJTSYYB000000001V0",
                "inboundOrderId": 21,
                "inboundOrderItemsId": 46,
                "orderSn": "RK2021012000000021",
                "remarks": "111",
                "unusualNum": 1,
                "unusualReasonId": 173,
                "warehouseId": 2
            }]
        }

        querystring = ""

        response = post_request(path=path, payload=payload, querystring=querystring)

        pprint.pprint(response)

    def tearDown(self) -> None:
        pass
