#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 14:59
# @Author  : limusem
# @File    : run_case.py
# @Software: PyCharm
# @Description:

import pytest

pytest.main(['-s','-v'])

# pytest.main(['-s', '-v', '-m system_test']) # 执行指定标签

# pytest.main(['-s', '-v', '-m system_test or smoke_test']) # 两个标签的用例都执行
#
# pytest.main(['-s', '-v', '-m system_test and smoke_test'])  #  包含两个标签的用例才执行
#
# pytest.main(['-s', '-v', '-m not system_test '])  #  除了该标签，其他用例都执行
