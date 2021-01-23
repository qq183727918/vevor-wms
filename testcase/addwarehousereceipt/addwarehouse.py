"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/20 15:34
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : add_warehouse.py
@Software  : PyCharm
"""

import pprint

import requests

from wmstoken.readtoken import read


class Warehousereceipt:

    def __init__(self):
        """
        预约新增，新增提交
        :return
        """

    @staticmethod
    def add_warehousereceipt():
        # 新增入库单
        path = "http://192.168.0.138:6084/api-iOverseasInboundService/outer/create"

        payload = {
            "sourceWarehouse": "上海常熟中转仓",
            "targetWarehouse": "美国",
            "seaChestNo": "QA0001",
            "sourceSn": "MAQ20210123001",
            "sourceCreatedBy": "肆意",
            "sourceCreatedTime": "2021-12-23 22:59:00",
            "sourceOutTime": "2021-12-29 21:18:00",
            "tenantId": "admin",
            "customerId": 85,
            "transType": 0,
            "operatorBy": 0,
            "operatorTime": "2021-01-17 21:18:00",
            "vos": [{
                "goodsSku": "QDJTSYYB000000001V0",
                "goodsName": "气动脚踏式液压泵",
                "num": 2,
                "sourceBatch": "NCG2019110510291",
                "length": 36,
                "width": 23,
                "height": 22,
                "weight": 7.84
            }, {
                "goodsSku": "97-02-1013QCXS001V0",
                "goodsName": "线束 97-02 1013汽车",
                "num": 8,
                "sourceBatch": "NCG2019110510292",
                "length": 36,
                "width": 25,
                "height": 20,
                "weight": 6.84
            }, {
                "goodsSku": "DG2000LBSHSYTDQ01V0",
                "goodsName": "吊钩 2000 lbs 黑色油桶吊钳",
                "num": 10,
                "sourceBatch": "NCG2019110510293",
                "length": 34,
                "width": 26,
                "height": 23,
                "weight": 6.45
            }]
        }
        token = read()
        querystring = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

        response = requests.post(url=path, json=payload, headers=querystring)

        re = response.json()

        pprint.pprint(re)


if __name__ == '__main__':
    wms = Warehousereceipt()
    wms.add_warehousereceipt()
