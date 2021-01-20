# _*_ coding: UTF-8 _*_
# @Time     : 2021/1/19 13:30
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : wms_params.py
# @Software : PyCharm

def test_url():
    """
    测试环境
    :return:
    """
    url = 'http://wms.test.vevor.net'

    return url


def debug_url():
    """
    调试地址
    :return:
    """
    url = 'http://192.168.0.138:6080'

    return url


def auth_url():
    """
    调试地址
    :return:
    """
    url = 'http://192.168.0.157:6081'

    return url


def preProduction_url():
    """
    预生产环境
    :return:
    """
    url = 'http://wms.preprod.vevor.net'

    return url


def produce_url():
    """
    生产环境
    :return:
    """
    url = 'http://wms.vevor.net'

    return url


def responseCode_two():
    """
    请求成功
    :return:
    """
    responseCode = [200, 404153]

    return responseCode


def responseCode_service():
    """
    服务存在问题
    :return:
    """
    responseCode = [401, 500, 530, 501, 110, 404, 403, 304001, 305003]

    return responseCode


def responseCode_develop():
    """
    token失效
    :return:
    """
    responseCode = {
        'code': 10010,
        'msg': '不是token问题，请联系开发人员',
        'data': '这是一个彩蛋谢谢！'
    }

    return responseCode


class Params:
    pass
