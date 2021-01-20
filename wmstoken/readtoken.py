# _*_ coding: UTF-8 _*_
# @Time     : 2021/1/19 11:55
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : readtoken.py
# @Software : PyCharm

def read():
    with open(r'D:\Tools\vevor\vevor-wms\wmstoken\token.txt', 'r')as f:
        token = f.read()

    print(token)
    return token


read()
