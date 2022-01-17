# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 8:01 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : 20210912_01_setting.py
# @Software: PyCharm
# @desc : 滑动app页面


import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import By

des = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "windwos虚拟机",
    "appPackage": "com.android.settings",
    "appActivity": "com.android.settings.Settings",
    "udid": "192.168.0.101:5555",
    "noReset": "True"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
driver.implicitly_wait(10)
# 需要先开启指针位置  tap([(a坐标x,a坐标y),(b坐标x,b坐标y)],滑动的时间)
# driver.tap([(720, 1910), (720, 1000), (720, 600)], 1000) # 轻轻的点击

touch = TouchAction(driver)
# touch.press(x=720, y=1910).perform()
#
# touch.long_press(x=720, y=1910).perform()

# touch.tap(x=720, y=1910).perform()

# driver.implicitly_wait(10)
# # 上滑操作 scroll  从一个元素移到另一个元素
# web_element_e1 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="帐号"]')
#
# web_element_e2 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="存储"]')
#
# # driver.scroll(web_element_e1, web_element_e2) # 滑动
# driver.drag_and_drop(web_element_e1, web_element_e2) # 拖动

"""

在使用滑动方法的时候，大多数情况都是使用道了坐标，坐标不好的地方在于不同的手机，代码兼容性差
因为手机屏幕的分辨木不一样

"""
#
# driver.flick(720, 1910, 720, 1000)  # 滑动 把 press 给成long_press  根据坐标滑动
# driver.swipe(720, 1910, 720, 1000,3000)
#
# size = driver.get_window_size()
# # print(size)
# driver.swipe(size['width'] / 2, size['height'] * 3 / 4, size['width'] / 2, size['height'] * 1 / 4, 2000)
#
# # # 等比例换算
# # driver.tap([(720, 1910)])
# # print(720 / size['width'], 1910 / size['height'])  # 会得到一个百分比
# #
# driver.tap([(int(size['width'] * 0.5), int(size['height'] * 0.68))])

# # 从下往上
# width = driver.get_window_size()['width']
# height = driver.get_window_size()['height']
# driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)
#
# # 从上往下
# width = driver.get_window_size()['width']
# height = driver.get_window_size()['height']
# driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)
#
# # 从左往右
# width = driver.get_window_size()['width']
# height = driver.get_window_size()['height']
# driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 500)
#
# # 从右往左
# width = driver.get_window_size()['width']
# height = driver.get_window_size()['height']
# driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 500)
