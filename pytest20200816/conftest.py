# -*- coding: utf-8 -*-
# @Time : 2021/9/17 16:26
# @Author : Limusen
# @File : conftest


"""

全局使用这个fixture

"""

import pytest


@pytest.fixture()
def set_up():
    print("测试初始化")
    yield
    print("测试环境清理")
