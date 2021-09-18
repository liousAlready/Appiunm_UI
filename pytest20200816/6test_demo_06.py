# -*- coding: utf-8 -*-
# @Time : 2021/9/17 16:23
# @Author : Limusen
# @File : test_demo_01

import os
import pytest

"""

pytest 执行测试报告

"""


@pytest.mark.skip(reason="设置测试类不执行")
class TestDemo06_01:

    @pytest.mark.skip(reason="开发未完善,阻碍测试")
    def test_add_01(self):
        print("~~~~ 哈哈哈哈哈哈哈 test_add_01 哈哈哈哈哈哈哈 ~~~~")
        assert True

    @pytest.mark.skipif(condition=True, reason="条件满足,用例不执行")
    def test_add_02(self):
        print("~~~~ 哈哈哈哈哈哈哈 test_add_02 哈哈哈哈哈哈哈 ~~~~")
        assert True

    def test_sub_01(self):
        print("~~~~ 哈哈哈哈哈哈哈 test_sub_01 哈哈哈哈哈哈哈 ~~~~")
        assert True

    def test_sub_02(self):
        print("~~~~ 哈哈哈哈哈哈哈 test_sub_02 哈哈哈哈哈哈哈 ~~~~")
        assert True


class TestDemo06_02:

    def test_add_01(self):
        print("~~~~ 哈哈哈哈哈哈哈 TestDemo05_02 test_add_01 哈哈哈哈哈哈哈 ~~~~")
        assert True

    def test_add_02(self):
        print("~~~~ 哈哈哈哈哈哈哈 TestDemo05_02 test_add_02 哈哈哈哈哈哈哈 ~~~~")
        assert True


if __name__ == '__main__':
    report_path = os.path.dirname(__file__) + "/allure_xml_report"
    print(report_path)
    pytest.main(['-s', '-v', '--alluredir=%s' % report_path])  # json格式的数据
    # allure generate ./allure_xml_report/-o ./allure_html_report/


