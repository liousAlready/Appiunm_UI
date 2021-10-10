#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 11:11
# @Author  : limusem
# @File    : run_case.py
# @Software: PyCharm
# @Description: 执行整个子包下符合条件的的测试用例

import pytest

# -s 打印print语句到控制台
# -v 显示测试用例的详细信息
pytest.main(["-s","-v"])  # pytest 会自动搜索当前文件夹以及子文件夹下所有满足编写规则的用例执行
