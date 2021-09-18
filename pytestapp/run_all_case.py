# -*- coding: utf-8 -*-
# @Time : 2021/9/18 9:27
# @Author : Limusen
# @File : run_all_case

import pytest

# 直接执行所有测试用例 不需要discover整合测试用例执行
pytest.main(['-s','-m smoketest'])
