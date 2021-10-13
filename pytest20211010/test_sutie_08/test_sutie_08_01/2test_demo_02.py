#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 15:01
# @Author  : limusem
# @File    : 2test_demo_02.py
# @Software: PyCharm
# @Description:

import pytest

"""

执行顺序按照放置的顺序：默认顺序

类也是一样执行
"""


class TestDemo02:

    @pytest.mark.smoke_test
    def test_case_06(self):
        print("exec : test_case_06  ", end="  ")
        assert True

    @pytest.mark.run(order=2)
    @pytest.mark.system_test
    def test_case_05(self):
        print("exec : test_case_05  ", end="  ")
        assert True


class TestDemo02_01:
    @pytest.mark.run(order=1)
    @pytest.mark.smoke_test
    def test_case_02_06(self):
        print("exec : test_case_02_06  ", end="  ")
        assert True
