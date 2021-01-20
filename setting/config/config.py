# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/19 20:24
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : config.py
# @Software : PyCharm
from config.wms_params import test_url
from config.wms_params import debug_url
from wmstoken.readtoken import read


def wms_config():
    l_config_url = debug_url()

    return l_config_url


def wms_headers():
    token = read()
    print(token)
    l_config_headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    return l_config_headers


if __name__ == '__main__':
    wms_config()
    wms_headers()
