#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 14:58
# @Author  : limusem
# @File    : 1test_demo_01.py
# @Software: PyCharm
# @Description:

import pytest


class TestDemo01:

    def test_case_01(self):
        print("exec : test_case_01  ", end="  ")
        assert True

    @pytest.mark.smoke_test
    @pytest.mark.login_module
    def test_case_02(self):
        print("exec : test_case_02  ", end="  ")
        assert True
