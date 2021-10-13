# -*- coding: utf-8 -*-
# @Time : 2021/10/13 14:07
# @Author : Limusen
# @File : login_test

import pytest
import allure


@allure.epic('[epic] 买买买商城系统')
@allure.feature("[feature] 你管我")
class TestLogin:
    @allure.story("[Story]用户根据用户名密码登录系统")
    @allure.title("[Title]case 01 正确的用户名密码登录")
    @allure.testcase(url="http://47.107.178.45/zentao/www/index.php?m=bug&f=view&bugID=686", name="用例地址")
    @allure.issue(url="http://47.107.178.45/zentao/www/index.php?m=bug&f=view&bugID=686", name="bug地址")
    @allure.description("登录测试用例 执行人：李某")
    @allure.link(url="http://www.baidu.com", name="百度一下，你就知道")
    @pytest.mark.logintest
    def test_login_success(self):
        print("exec test_login_success :安装apk成功,很棒!", end=" ")
        assert True

    @allure.story("[Story]用户根据用户名密码登录系统")
    @allure.title("[Title]case 01 正确的用户名密码登录")
    @allure.description("登录测试用例 执行人：李某")
    # @pytest.mark.skip("无条件跳过...")
    @pytest.mark.logintest
    def test_login_fail(self):
        print("exec test_login_fail :安装apk失败,请检查相关配置问题噢...", end=" ")
        assert True

