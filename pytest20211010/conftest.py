#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 14:46
# @Author  : limusem
# @File    : conftest.py
# @Software: PyCharm
# @Description:  将fixture放入此文件 则引用fixture名称的函数会自动调用fixture


import pytest


@pytest.fixture(params=[1, 2, 3, 4, 5], ids=['num1', 'num2', 'num3', 'num4', 'num5', ])
def fixture_function(request):
    return request.param
