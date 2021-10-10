#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 11:06
# @Author  : limusem
# @File    : 1test_demo_01.py
# @Software: PyCharm
# @Description:  param 参数化使用

import pytest


@pytest.fixture(params=[(1, 2, 3), (4, 5, 9), (10, 20, 30)])
def fixture_function(request):
    return request.param


class TestDemo05:
    def test_case_01(self, fixture_function):
        print("%d + %d ?= %d " % (fixture_function[0], fixture_function[1], fixture_function[2]), end= "  ")
        assert fixture_function[0] + fixture_function[1] == fixture_function[2]


if __name__ == '__main__':
    pytest.main()  # 执行
