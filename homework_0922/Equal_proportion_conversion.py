# -*- coding: utf-8 -*-
# @Time : 2021/9/24 14:47
# @Author : Limusen
# @File : Equal_proportion_conversion

import time
from appium import webdriver
from appium.webdriver.webdriver import By
from appium.webdriver.common.touch_action import TouchAction
import pytest

"""

https://blog.csdn.net/weixin_42335807/article/details/114910849?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522163246610716780366593856%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=163246610716780366593856&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-4-114910849.first_rank_v2_pc_rank_v29&utm_term=appium+%E7%AD%89%E6%AF%94%E4%BE%8B%E6%8D%A2%E7%AE%97&spm=1018.2226.3001.4187

"""

des = {
    "platformName": "Android",
    "platformVersion": "8.1.0",
    "deviceName": "vivo x20",
    "appPackage": "com.android.settings",
    "appActivity": "com.android.settings.Settings",
    "udid": "c6c8c4ce",
    "noReset": True,
    "newCommandTimeout": 30  # 30s没对手机发送新命令，就断开连接
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
driver.implicitly_wait(10)

size = driver.get_window_size()

x = size['width']
y = size['height']
print(x, y)

x1 = int(x / 2)
y_start = int(y * 4 / 5)
y_end = int(y * 1 / 5)

# # 等比例移动
# TouchAction(driver).long_press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

driver.swipe(start_x=x1, start_y=y_start, end_x=x1, end_y=y_end)
