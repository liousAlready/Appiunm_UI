# -*- coding: utf-8 -*-
# @Time : 2021/9/17 16:23
# @Author : Limusen
# @File : test_demo_01

import os
import pytest
import allure

"""

自定义测试类名

"""


@allure.story("P1P2测试类")  # 给测试类定义名字
class TestDemo06_01:

    def test_add_01(self):
        print("~~~~ 哈哈哈哈哈哈哈 test_add_01 哈哈哈哈哈哈哈 ~~~~")
        assert True

    def test_add_02(self):
        print("~~~~ 哈哈哈哈哈哈哈 test_add_02 哈哈哈哈哈哈哈 ~~~~")
        assert True


if __name__ == '__main__':
    report_path = os.path.dirname(__file__) + "/allure_xml_report"
    report_html_path = os.path.dirname(__file__) + "/allure_html_report"
    pytest.main(['-s', '-v', '--alluredir=%s' % report_path])  # json格式的数据
    os.system('allure generate %s -o %s' % (report_path, report_html_path))
