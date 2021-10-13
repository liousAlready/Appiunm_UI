#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 11:11
# @Author  : limusem
# @File    : run_case.py
# @Software: PyCharm
# @Description: 执行整个子包下符合条件的的测试用例

import pytest
import os

# -s 打印print语句到控制台
# -v 显示测试用例的详细信息
# pytest.main(["-s","-v"])  # pytest 会自动搜索当前文件夹以及子文件夹下所有满足编写规则的用例执行

# pytest.main(['-s','-v','--junit-xml=log.xml'])

# pytest.main(['-s','-v','--html=resutl.html'])

"""

allure 使用步骤

1.先生成json文件
pytest.main(['-s','-v','--alluredir=./allure_json_path'])

2.执行allure语句，生成allure_html_path
allure generate ./allure_json_path -o ./allure_html_path

3.再次执行allure语句会报错已存在 所以需要添加 --clean  这个是清除 allure_html_path 中的html文件
allure generate ./allure_json_path -o ./allure_html_path --clean

4.由于每次执行之后json文件都会保留，会影响查看，所以要清除缓存  此 --clean-alluredir 是清除allure_json_path 里面的json文件
pytest.main(['-s', '-v', '--alluredir=./allure_json_path','--clean-alluredir'])

5.使用python执行dos命令

"""

pytest.main(['-s', '-v', '--alluredir=./allure_json_path', '--clean-alluredir'])

os.system('allure generate %s -o %s --clean' % ("./allure_json_path", "./allure_html_path"))
