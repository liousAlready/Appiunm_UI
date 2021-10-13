# -*- coding: utf-8 -*-
# @Time : 2021/10/13 14:05
# @Author : Limusen
# @File : conftest

import os

import pytest

# # 执行logintest/systemtest用例
# pytest.main(['-s', '-v', '-m logintest and systemtest'])

pytest.main(['-s', '-v', '--alluredir=./allure_json_path', '--clean-alluredir'])

os.system('allure generate %s -o %s --clean' % ("./allure_json_path", "./allure_html_path"))
