# _*_ coding: UTF-8 _*_
# @Time     : 2021/1/19 11:55
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : judgmentFailure.py
# @Software : PyCharm
def judgmentFailure(code):
    if code == 200:
        print('token可以正常使用')
    elif code == 401:
        print('token失效')
    elif code == 500:
        print('请联系开发人员解决')
    elif code == 503:
        print('请联系开发人员解决')
    elif code == 110:
        print('请联系开发人员解决')
    else:
        print('请联系开发人员解决')


if __name__ == '__main__':
    code = 401
    judgmentFailure(code)
