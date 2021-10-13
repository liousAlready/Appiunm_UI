#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 11:06
# @Author  : limusem
# @File    : 1test_demo_01.py
# @Software: PyCharm
# @Description:  param 参数化使用

import pytest


@pytest.fixture(params=[1, 2, 3, 4, 5],ids=['num1','num2','num3','num4','num5',])
def fixture_function(request):
    return request.param


class TestDemo04:
    def test_case_01(self, fixture_function):
        print("exec test_case, use %d " % fixture_function, end=" ")
        assert True


if __name__ == '__main__':
    pytest.main()  # 执行
