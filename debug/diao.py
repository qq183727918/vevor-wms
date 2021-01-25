"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/25 17:36
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : diao.py
@Software  : PyCharm
"""

import requests

url = 'https://gatewaypreprod.vevor.net/scp-inventory-service/controller-transferInventoryDetailService/warehouseGoods/70?destinationWarehouse=4PX-%E6%8D%B7%E5%85%8B%E4%BB%93&deliverWarehouseId=1'

querystring = {
    "destinationWarehouse": "%E7%BE%8E%E5%9B%BD-FBA-salesupermarket@outlook.com",
    "deliverWarehouseId": 1
}
payload = []
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 55704b53-b177-4114-8415-a9fba1fd1015"

}
response = requests.post(url, headers=headers, json=payload, params=querystring)

re = response.json()

# pprint.pprint(re)

lists = re['data']
for i in lists:
    batchCode = i['batchCode'] + '\n'
    with open('./test.csv', 'a')as f:
        f.write(batchCode)
