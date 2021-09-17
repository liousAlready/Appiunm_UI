# -*- coding: utf-8 -*-
# @Time : 2021/9/17 15:39
# @Author : Limusen
# @File : test_demo_02

import pytest


@pytest.fixture()  # 测试初始化
def set_up():
    print("这是初始化")
    yield  # 测试环境清理 关键字
    print("测试环境清理")


class TestDemo02:
    def test_add(self, set_up):  # set_up 为初始化方法名称
        print('exec TestDemo02 test_add')
        assert 10 + 10 == 20

    def test_sub(self, set_up):  # set_up 为初始化方法名称
        print('exec TestDemo02 test_add')
        assert 10 - 10 == 20


if __name__ == '__main__':
    pytest.main(['-s'])  # -s 显示print信息
