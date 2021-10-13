#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 15:01
# @Author  : limusem
# @File    : 1test_demo_01.py
# @Software: PyCharm
# @Description:

import pytest


class TestDemo01:
    @pytest.mark.system_test
    def test_case_03(self):
        print("exec : test_case_03  ", end="  ")
        assert True

    def test_case_04(self):
        print("exec : test_case_04  ", end="  ")
        assert True
