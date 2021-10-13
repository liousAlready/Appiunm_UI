#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 17:00
# @Author  : limusem
# @File    : test_commodity.py
# @Software: PyCharm
# @Description:

import allure


@allure.epic("[Epic]好再来电商系统")
@allure.feature("[Feature]好再来电商系统 V1.9.1")
class TestCommodity:
    @allure.story("[Story]商品模块新增商品")
    @allure.title("[Title]case 01 新增商品至商品中心")
    def test_commodity_add(self):
        pass
        assert True

    @allure.story("[Story]商品模块新增商品")
    @allure.title("[Title]case 02 新增商品至中台")
    def test_commodity_create(self):
        pass
        assert True
