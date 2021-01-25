"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/24 11:43
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : debug.py
@Software  : PyCharm
"""

import unittest

from BeautifulReport import BeautifulReport

# 用例存放位置
test_case_path = r"D:\Tools\vevor\vevor-wms\debug"
# 测试报告存放位置
log_path = r'D:\Tools\vevor\vevor-wms\report'
# 测试报告名称
filename = '测试报告2'
# 用例名称
description = '刘晓强测试'
# 需要执行哪些用例，如果目录下的全部，可以改为"*.py"，如果是部分带test后缀的，可以改为"*test.py"
pattern = "*.py"

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover(test_case_path, pattern=pattern)
    result = BeautifulReport(test_suite)
    result.report(filename=filename, description=description, report_dir=log_path)
