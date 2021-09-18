# -*- coding: utf-8 -*-
# @Time : 2021/9/17 16:23
# @Author : Limusen
# @File : test_demo_01


import pytest
"""

@pytest.mark.smoketest 指定标签

"""

@pytest.mark.smoketest
def test_add_01():
    print("~~~~ 哈哈哈哈哈哈哈 test_add_01 哈哈哈哈哈哈哈 ~~~~")
    assert True


def test_add_02():
    print("~~~~ 哈哈哈哈哈哈哈 test_add_02 哈哈哈哈哈哈哈 ~~~~")
    assert True


@pytest.mark.smoketest
def test_sub_01():
    print("~~~~ 哈哈哈哈哈哈哈 test_sub_01 哈哈哈哈哈哈哈 ~~~~")
    assert True


def test_sub_02():
    print("~~~~ 哈哈哈哈哈哈哈 test_sub_02 哈哈哈哈哈哈哈 ~~~~")
    assert True


if __name__ == '__main__':
    pytest.main(['-s','-m smoketest']) # -m 标签名 指定标签
