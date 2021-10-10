#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 11:06
# @Author  : limusem
# @File    : 1test_demo_01.py
# @Software: PyCharm
# @Description:  fixture的用法

import pytest


# function 每个函数执行一次
# class  执行类级别
# module 执行模块级别
# autouse = True 自动执行fixture不需要手动在用例上添加
# name = sss  直接调用名字 调用原方法名称会报错不存在


# @pytest.fixture(scope="module", autouse=True)


@pytest.fixture(scope="class", name="sss")
def fixture_function():
    print("测试用例开始之前执行", end=" ")
    yield
    print("   测试用例开始之后执行", end=" ")


class TestDemo03:
    def test_case_01(self,sss):
        print("exec test_case_01", end=" ")
        assert 1 + 3 == 4

    def test_case_02(self):
        print("exec test_case_02", end=" ")
        assert 2 + 3 == 5


class TestDemo03_01:
    def test_case_01(self):
        print("exec test_case_03_01", end=" ")
        assert 1 + 3 == 4

    def test_case_02(self,sss):
        print("exec test_case_03_02", end=" ")
        assert 2 + 3 == 5


if __name__ == '__main__':
    pytest.main()  # 执行
