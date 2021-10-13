# -*- coding: utf-8 -*-
# @Time : 2021/10/13 14:54
# @Author : Limusen
# @File : login_smoke

import pytest


class TestLoginSmoke:

    def test_smoke_login_button(self):
        print("测试登录按钮是否可以点击", end=" ")
        assert True

    def test_smoke_login_username_input(self):
        print("测试登录的用户名输入框是否能够输入", end=" ")
        assert True

    def test_smoke_login_password_input(self):
        if True:
            pytest.skip("内部方法跳过测试用例")
        print("测试登录的用户名输入框是否能够输入", end=" ")
        assert True
