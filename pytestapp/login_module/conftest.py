# -*- coding: utf-8 -*-
# @Time : 2021/9/17 16:32
# @Author : Limusen
# @File : conftest


import pytest


# 顶层的conftest 一般是针对各个子包运行一次
# 包层次(大模块)的conftest 一般是针对各个子包运行一次
@pytest.fixture(scope='module', autouse=True)
def set_up_module():
    print("~~ test module test start run ~~")
    yield
    print("~~ test module test end run ~~")
