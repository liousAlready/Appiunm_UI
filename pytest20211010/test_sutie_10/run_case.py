#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 16:59
# @Author  : limusem
# @File    : run_case.py
# @Software: PyCharm
# @Description:


import os
import pytest

pytest.main(['-s', '-v', '--alluredir=./allure_json_path', '--clean-alluredir'])
os.system('allure generate %s -o %s --clean' % ("./allure_json_path", "./allure_html_path"))
