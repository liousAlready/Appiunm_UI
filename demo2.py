# -*- coding: utf-8 -*-
# @Time : 2021/9/7 17:55
# @Author : Limusen
# @File : demo2

import os

# https://pypi.douban.com/simple  # 豆瓣镜像
# https://pypi.tuna.tsinghua.edu.cn/simple  # 清华镜像

mirror = " -i https://pypi.douban.com/simple"

os.system("python -m pip install --upgrade pip" + mirror)  # 更新 pip
os.system("pip install --pre -U uiautomator2" + mirror)  # 安装 uiautomator2
os.system("pip install --pre weditor" + mirror)  # 安装 weditor
os.system("python -m uiautomator2 init")  # 安装 atx-agent 至手机