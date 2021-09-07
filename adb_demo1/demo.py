# -*- coding: utf-8 -*-
# @Time : 2021/9/3 9:58
# @Author : Limusen
# @File : demo

import time
from appium import webdriver

# des = {
#     'platformName': 'Android',
#     'platformVersion': '9.0',
#     'deviceName': 'Samsung Galaxy S9',
#     'appPackage': 'com.android.calculator2',  # 包名
#     'appActivity': 'com.android.calculator2.Calculator',  # app入口
#     'udid': '192.168.105.102:5555',  # genymotion设备
#     'noReset': True,
#     'unicodeKeyboard': True,
#     'resetKeyboard': True,
# }

des = {  # 简单计算器绿色的
    "platformName": "Android",
    "platformVersion": "10.0",
    "deviceName": "小米",
    "appPackage": "rock.Simple.Calculator",
    "appActivity": "rock.Simple.Calculator.MainActivity",
    "udid": "7592904",
    "noReset": True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
}

# des = {
#     "platformName": "Android",
#     "platformVersion": "10.0",
#     "deviceName": "小米",
#     "appPackage": "com.sky.jisuanji",
#     "appActivity": ".JisuanjizixieActivity",
#     "udid": "7592904",
#     "noReset": True,
#     "unicodeKeyboard": True,
#     "resetKeyboard": True,
# }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)

driver.find_element_by_id('rock.Simple.Calculator:id/nine_btn').click()
driver.find_element_by_id('rock.Simple.Calculator:id/add_btn').click()
driver.find_element_by_id('rock.Simple.Calculator:id/eight_btn').click()
driver.find_element_by_id('rock.Simple.Calculator:id/equal_btn').click()

# 　class定位
driver.find_element_by_class_name('android.widget.LinearLayout').click()

# driver.find_element_by_accessibility_id('删除').click()

# 　注意开头要使用双斜杠　绝对路径　遇到相通的元素使用下标来标识　　/hierarchy
driver.find_element_by_xpath('//android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.Button[2]').click()
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.Button[2]').click()

# 属性定位   //类名[@属性名='属性值']
driver.find_element_by_xpath('//android.widget.Button[@text="5"]').click()
# 多属性定位   //类名[@属性名='属性值' and/or @属性名='属性值'] 可以使用多个属性值定位 用and进行连接
driver.find_element_by_xpath('//android.widget.Button[@index="1" and @text="5"]').click()

time.sleep(1)
# 部分属性定位
driver.find_element_by_xpath('//android.widget.Button[contains(@resource-id,"nine_btn")]').click()
time.sleep(1)
# 已某某元素结尾
driver.find_element_by_xpath('//android.widget.Button[ends-with(@resource-id,"seven_btn")]').click()
# # 起始位置匹配
# driver.find_element_by_xpath('//android.widget.Button[starts-with()]').click()

# # 调用UiAutomator 失效
# driver.find_element_by_android_uiautomator("text('9')").click()
# driver.find_element_by_android_uiautomator("new UiSelector().resourceId('rock.Simple.Calculator:id/eight_btn')").click()

