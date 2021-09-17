# -*- coding: utf-8 -*-
# @Time : 2021/9/17 15:29
# @Author : Limusen
# @File : testdemo01

import pytest


class TestDemo01:

    def test_add(self):
        assert 10 + 10 == 20


if __name__ == '__main__':
    pytest.main()
