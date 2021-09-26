# -*- coding: utf-8 -*-
# @Time : 2021/9/17 16:23
# @Author : Limusen
# @File : test_demo_01

import os
import pytest
import allure
import shutil


@pytest.fixture(autouse=True)
def set_up():
    print("前置条件: *** ")
    yield
    print("后置条件: *** ")


@allure.step("步骤一:打开被测试app")
def one_step():
    pass


@allure.step("步骤二:不输入用户名密码")
def two_step():
    pass


@allure.step("步骤二:输入正确的用户名密码")
def twos_step():
    pass


@allure.epic("[epic]张麻子电商V1.0")
@allure.feature("[feature]登录模块")
class TestLogin:
    @allure.story("[story]不输入用户名和密码")
    @allure.title("[case 01] 不使用账号跟密码登录系统")
    def test_login_01(self):
        one_step()
        two_step()
        print("~~~~ 哈哈哈哈哈哈哈 test_add_01 哈哈哈哈哈哈哈 ~~~~")
        assert True

    @allure.story("[story]输入正确的用户名和密码")
    @allure.title("[case 02] 使用admin\\123456登录系统")
    @allure.testcase("http://192.168.31.200:8888/zentao/bug-view-626.html", "禅道测试用例地址")  # 测试用例的路径，可以跳转到对网页
    @allure.issue("http://192.168.31.200:8888/zentao/bug-view-626.html", "禅道bug地址")  # bug地址
    @allure.link("http://www.baidu.com", name='百度一下,你就知道')  #
    @allure.description("正向场景用例 ")  # 描述信息
    # @allure.severity('blocker') # 测试用例的优先级
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_02(self):
        one_step()
        twos_step()
        # allure.step("zzz") 不行
        with allure.step("步骤三:点击登录按钮"):  # 需要用with进行包裹输出
            print("~~~~ 哈哈哈哈哈哈哈 test_add_02 哈哈哈哈哈哈哈 ~~~~")
        with allure.step("步骤四:上传附件"):  # 需要用with进行包裹输出
            print("~~~~ 哈哈哈哈哈哈哈 test_add_02 哈哈哈哈哈哈哈 ~~~~")
        with open(os.path.dirname(__file__) + "/screen_shot/iu.jpg", "rb") as file:  # 上传附件
            file_img = file.read()
            allure.attach(file_img, "色色图片", allure.attachment_type.PNG)
        assert True


@allure.epic("[epic]张麻子电商V1.0")
@allure.feature("[feature]商品")
class TestCommodity:
    @allure.title("[case 01] 正常添加商品信息")
    def test_commodity_01(self):
        print("~~~~ 哈哈哈哈哈哈哈 test_Commodity_01 哈哈哈哈哈哈哈 ~~~~")
        assert True

    @allure.title("[case 02] 不添加商品信息")
    def test_commodity_02(self):
        print("~~~~ 哈哈哈哈哈哈哈 test_Commodity_02 哈哈哈哈哈哈哈 ~~~~")
        assert True


@allure.epic("[epic]黑麻子电商V1.0")
@allure.feature("[feature]商品")
class TestGem:
    @allure.title("[case 01] 正常添加商品信息")
    def test_commodity_01(self):
        print("~~~~ 哈哈哈哈哈哈哈 test_Commodity_01 哈哈哈哈哈哈哈 ~~~~")
        assert True

    @allure.title("[case 02] 不添加商品信息")
    def test_commodity_02(self):
        print("~~~~ 哈哈哈哈哈哈哈 test_Commodity_02 哈哈哈哈哈哈哈 ~~~~")
        assert True


if __name__ == '__main__':
    report_path = os.path.dirname(__file__) + "/allure_xml_report"
    report_html_path = os.path.dirname(__file__) + "/allure_html_report"
    if os.path.isdir(report_path):
        shutil.rmtree(report_path)
    os.mkdir(report_path)
    # pytest.main(['-s', '-v', '--alluredir=%s ' % report_path, "--allure-epics=[epic]黑麻子电商V1.0"])  # 执行指定的项目层
    # pytest.main(['-s', '-v', '--alluredir=%s ' % report_path, "--allure-features=[feature]商品"])  # 执行的feature
    pytest.main(['-s', '-v', '--alluredir=%s ' % report_path, "--allure-stories=[story]输入正确的用户名和密码"])  # 执行指定的故事层


    os.system('allure generate %s -o %s --clean' % (report_path, report_html_path))
