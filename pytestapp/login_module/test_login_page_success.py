# -*- coding: utf-8 -*-
# @Time : 2021/9/17 16:30
# @Author : Limusen
# @File : test_login_succest

import pytest


class TestLoginPageCases:
    @pytest.mark.smoketest
    @pytest.mark.run(order=1)
    def test_login_page_01(self):
        print("~~ exec test_login_page_01 TestLoginCases ~~")
        assert True

    @pytest.mark.logintest
    def test_login_page_02(self):
        print("~~ exec test_login_page_02 TestLoginCases ~~")
        assert True
