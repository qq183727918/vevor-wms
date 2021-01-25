# """
# _*_ coding: UTF-8 _*_
# @Time      : 2021/1/24 11:00
# @Author    : LiuXiaoQiang
# @Site      : https://github.com/qq183727918
# @File      : singleItem_detail_select.py
# @Software  : PyCharm
# """
#
# import pprint
#
# from setting.wms_requests.wms_data_get import get_request
#
#
# class singleItem_detail_select:
#
#     def __init__(self):
#         """
#         单品拣货详情查询
#         :return
#         """
#
#     @staticmethod
#     def singleItem_detail_select():
#         path = ''
#
#         payload = ""
#
#         querystring = {
#         }
#
#         response = get_request(path=path, payload=payload, querystring=querystring)
#
#         pprint.pprint(response)
#
#
# if __name__ == '__main__':
#     wms = singleItem_detail_select()
#     wms.singleItem_detail_select()
