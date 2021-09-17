# -*- coding: utf-8 -*-
# @Time : 2021/9/17 16:23
# @Author : Limusen
# @File : test_demo_01


import pytest


# @pytest.fixture(autouse=True)
# def set_up():
#     print("测试初始化")
#     yield
#     print("测试环境清理")


def test_sub():
    print("~~~~ 哈哈哈哈哈哈哈 test_sub 哈哈哈哈哈哈哈 ~~~~")
    assert True


if __name__ == '__main__':
    pytest.main(['-s'])
