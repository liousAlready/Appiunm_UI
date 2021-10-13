# -*- coding: utf-8 -*-
# @Time : 2021/10/13 14:56
# @Author : Limusen
# @File : system_tset

import pytest

class TestSystem:
    @pytest.mark.systemtest
    def test_system(self):
        print("系统测试", end=" ")
        assert True
