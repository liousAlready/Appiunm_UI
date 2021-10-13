#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 11:06
# @Author  : limusem
# @File    : 1test_demo_01.py
# @Software: PyCharm
# @Description:  param 参数化使用


class TestDemo07:
    def test_case_07(self, fixture_function):
        print("07: exec test_case, use %d " % fixture_function, end=" ")
        assert True
