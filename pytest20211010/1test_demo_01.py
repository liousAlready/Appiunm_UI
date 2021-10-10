#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 11:06
# @Author  : limusem
# @File    : 1test_demo_01.py
# @Software: PyCharm
# @Description: 测试方法的写法

import pytest


def add(num1, num2):  # 待测试的函数
    return num1 + num2


def test_case_01():  # 测试方法 == 》 测试用例
    assert add(3, 4) == 7  # assert 断言语句  add(3,4) 实际结果  7 期望结果


if __name__ == '__main__':
    pytest.main()  # 执行
