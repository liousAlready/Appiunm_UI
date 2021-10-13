#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 11:06
# @Author  : limusem
# @File    : 1test_demo_01.py
# @Software: PyCharm
# @Description:  param 参数化使用

import pytest

"""

测试用例跳过设置 

@pytest.mark.skip("无条件跳过")

@pytest.mark.skipif([1, 2, 3], reason="条件成立跳过")  # if 非空  非0 True 逻辑运算 3>2

if True:
    pytest.skip("内部方法跳过")

pytestmark = pytest.mark.skip("无条件跳过所有的测试用例！！！") # 跳过所有的用例

"""


# pytestmark = pytest.mark.skip("无条件跳过所有的测试用例！！！") # 跳过所有的用例

class TestDemo09:
    # @pytest.mark.skip("无条件跳过")
    def test_case_01(self):
        print("09-01   : exec test_case_01 ", end=" ")
        assert True

    # @pytest.mark.skipif([1, 2, 3], reason="条件成立跳过")  # if 非空  非0 True 逻辑运算 3>2
    def test_case_02(self):
        print("09-02   : exec test_case_02 ", end=" ")
        assert True

    def test_case_03(self):
        if True:
            pytest.skip("内部方法跳过")
        print("09-03   : exec test_case_03 ", end=" ")
        assert True

    def test_case_04(self):
        print("09-04   : exec test_case_04 ", end=" ")
        assert True


