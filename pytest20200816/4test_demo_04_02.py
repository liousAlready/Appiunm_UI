# -*- coding: utf-8 -*-
# @Time : 2021/9/17 16:23
# @Author : Limusen
# @File : test_demo_01


import pytest

"""

@pytest.mark.run(order=顺序)   控制标签

可以跨文件执行


"""


@pytest.mark.run(order=1)
def test_add_01():
    print("~~~~ 哈哈哈哈哈哈哈 test_add_01 哈哈哈哈哈哈哈 ~~~~")
    assert True


@pytest.mark.run(order=4)
def test_add_02():
    print("~~~~ 哈哈哈哈哈哈哈 test_add_02 哈哈哈哈哈哈哈 ~~~~")
    assert True


@pytest.mark.run(order=3)
def test_sub_01():
    print("~~~~ 哈哈哈哈哈哈哈 test_sub_01 哈哈哈哈哈哈哈 ~~~~")
    assert True


@pytest.mark.run(order=2)
def test_sub_02():
    print("~~~~ 哈哈哈哈哈哈哈 test_sub_02 哈哈哈哈哈哈哈 ~~~~")
    assert True


if __name__ == '__main__':
    pytest.main(['-s', '-v'])  # -m 标签名 指定标签
