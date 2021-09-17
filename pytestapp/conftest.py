# -*- coding: utf-8 -*-
# @Time : 2021/9/17 16:32
# @Author : Limusen
# @File : conftest

import pytest


# 顶层的conftest 一般是针对各个子包运行一次

@pytest.fixture(scope='package', autouse=True)
def set_up():
    print("~~ test package test start run ~~")
    yield
    print("~~ test package test end run ~~")
