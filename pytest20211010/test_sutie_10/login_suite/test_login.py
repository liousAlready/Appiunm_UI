#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 17:00
# @Author  : limusem
# @File    : test_login.py
# @Software: PyCharm
# @Description:  allure 方法描述使用


import allure


@allure.step("步骤一：打开好再来电商系统")  # 步骤
def step_01():
    pass


@allure.epic("[Epic]好再来电商系统")
@allure.feature("[Feature]好再来电商系统 V1.9.1")
class TestLogin:
    @allure.story("[Story]用户根据用户名密码登录系统")
    @allure.title("[Title]case 01 正确的用户名密码登录")
    @allure.testcase(url="http://47.107.178.45/zentao/www/index.php?m=bug&f=view&bugID=686", name="用例地址")
    @allure.issue(url="http://47.107.178.45/zentao/www/index.php?m=bug&f=view&bugID=686", name="bug地址")
    @allure.description("登录测试用例 执行人：李某")
    @allure.link(url="http://www.baidu.com", name="百度一下，你就知道")
    # @allure.severity_level("normal")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_success(self):
        step_01()
        with allure.step("步骤二：输入用户名：admin"):
            pass
        with allure.step("步骤三：输入密码：123456"):
            pass
        with open(r'D:\Appiunm_UI\pytest20211010\test_sutie_10\login_suite\test.jpg', "rb") as img_file:
            img_file_obj = img_file.read()
            allure.attach(img_file_obj, "测试报错截图", allure.attachment_type.JPG)
        assert True

    @allure.story("[Story]用户根据用户名密码登录系统")
    @allure.title("[Title]case 02 错误的用户名密码登录")
    def test_login_fail(self):
        pass
        assert True
