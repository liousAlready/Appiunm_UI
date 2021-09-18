# -*- coding: utf-8 -*-
# @Time : 2021/9/17 16:23
# @Author : Limusen
# @File : test_demo_01


import pytest

"""
跳过用例的执行方法

1.@pytest.mark.skip(reason="开发未完善,阻碍测试")  无条件跳过
2.@pytest.mark.skipif(condition=True, reason="条件满足,用例不执行")  条件满足的情况跳过
3.方法级别
def test_sub_01():
    pytest.skip("无条件跳过") # 跳过
    print("~~~~ 哈哈哈哈哈哈哈 test_sub_01 哈哈哈哈哈哈哈 ~~~~")
    assert True

模块级别
4.pytestmark = pytest.mark.skip()  # 此语句屏蔽模块下所有类及方法跳过

5.类级别
@pytest.mark.skip(reason="设置测试类不执行")
class TestDemo05:

    @pytest.mark.skip(reason="开发未完善,阻碍测试")
    def test_add_01(self):
        print("~~~~ 哈哈哈哈哈哈哈 test_add_01 哈哈哈哈哈哈哈 ~~~~")
        assert True

"""

pytestmark = pytest.mark.skip()  # 此语句屏蔽模块下所有类及方法跳过


@pytest.mark.skip(reason="设置测试类不执行")
class TestDemo05:

    @pytest.mark.skip(reason="开发未完善,阻碍测试")
    def test_add_01(self):
        print("~~~~ 哈哈哈哈哈哈哈 test_add_01 哈哈哈哈哈哈哈 ~~~~")
        assert True

    @pytest.mark.skipif(condition=True, reason="条件满足,用例不执行")
    def test_add_02(self):
        print("~~~~ 哈哈哈哈哈哈哈 test_add_02 哈哈哈哈哈哈哈 ~~~~")
        assert True

    def test_sub_01(self):
        if True:
            pytest.skip("无条件跳过")
        print("~~~~ 哈哈哈哈哈哈哈 test_sub_01 哈哈哈哈哈哈哈 ~~~~")
        assert True

    def test_sub_02(self):
        print("~~~~ 哈哈哈哈哈哈哈 test_sub_02 哈哈哈哈哈哈哈 ~~~~")
        assert True


class TestDemo05_02:

    def test_add_01(self):
        print("~~~~ 哈哈哈哈哈哈哈 TestDemo05_02 test_add_01 哈哈哈哈哈哈哈 ~~~~")
        assert True

    def test_add_02(self):
        print("~~~~ 哈哈哈哈哈哈哈 TestDemo05_02 test_add_02 哈哈哈哈哈哈哈 ~~~~")
        assert True


if __name__ == '__main__':
    pytest.main(['-s', '-v'])  # -m 标签名 指定标签
