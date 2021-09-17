# -*- coding: utf-8 -*-
# @Time : 2021/9/17 15:39
# @Author : Limusen
# @File : test_demo_02

import pytest


# 参数化
@pytest.fixture(ids=['01', '02', '03'], params=[100, 200, 300])
def set_up(request):  # 一定要request
    return request.param


class TestDemo07:
    def test_add(self, set_up):  # set_up 为初始化方法名称
        print('exec TestDemo07 test_add')
        assert 100 + 100 <= set_up


if __name__ == '__main__':
    pytest.main(['-v','-s'])  # -s 显示print信息 -v 查看全部日志
