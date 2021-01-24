# _*_ coding: UTF-8 _*_
# @Time     : 2021/1/19 11:55
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : judgmentFailure.py
# @Software : PyCharm
from wmstoken.gaintoken import gainToken


def judgmentFailure(code):
    if code == 200:
        print('token可以正常使用')
        return 200
    elif code == 401:
        print('token失效,正在重新获取，请稍等...')
        codes = gainToken()
        print('token获取成功,请重试...')
        judgmentFailure(codes)
        return 401
    elif code == 305003:
        print('服务暂不可用，请稍后重试或联系管理员')
        return 305003
    elif code == 503:
        print('服务挂了，请重新启动')
        return 503
    elif code == 110:
        print('系统异常')
        return 110
    else:
        print('请联系开发人员解决')


if __name__ == '__main__':
    code = 401
    judgmentFailure(code)
