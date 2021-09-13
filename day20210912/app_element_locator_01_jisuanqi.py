# -*- coding: utf-8 -*-
# @Time    : 2021/9/8 8:36 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : des_setting_demo_01.py
# @Software: PyCharm
# @desc : adb  识别元素定位

from appium import webdriver
from appium.webdriver.webdriver import By

des = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "mac虚拟机",
    "appPackage": "com.android.calculator2",
    "appActivity": "com.android.calculator2.Calculator",
    "udid": "192.168.56.104:5555",
    "noReset": "True"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)

# # id 定位可以去 resource-id  id  name
# driver.find_element_by_id("com.android.calculator2:id/digit_9").click()
# #  新写法
# driver.find_element(By.ID, "com.android.calculator2:id/digit_9").click()

# # 按乘号
# driver.find_element_by_accessibility_id('×').click()  # content-desc属性
#
# # xpath是一门标记语言 作用在XML、XHTML文档中查找元素
# # selenium Xpath是1.0版本  appium Xpath是2.0版本语法
#
# # 方法一： 绝对路径 / 开头 从根节点找元素 遇到同层级相同元素用下标区分，下标从1开始
# driver.find_element_by_xpath(
#     '//android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/'
#     'android.widget.LinearLayout[2]/android.view.ViewGroup[1]/android.widget.Button[2]').click()

# # 方法二：使用 属性 定位 //类名[@属性名="属性值"]
# driver.find_element(By.XPATH, '//android.widget.Button[@text="7"]').click()
#
# driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.android.calculator2:id/digit_7"]').click()
#
# # 扩展：多个属性定位  //类名[@属性名1="属性值1" and @属性名2="属性值2"]   都成立
# # //类名[@属性名1="属性值1" or @属性名2="属性值2"] 两个其中一个就行
# driver.find_element(By.XPATH,
#                     '//android.widget.Button[@text="9" and @bounds="[610,1637][886,1918]"]').click()
#
# driver.find_element(By.XPATH,
#                     '//android.widget.Button[@text="1" or @bounds="[12k3]"]').click()
#
# # find_elements 把满足条件的所有元素按匹配顺序放入列表
# els = driver.find_elements(By.XPATH,
#                            '//android.widget.Button[@text="9" or @text="8"]')
# els[0].click()
# els[1].click()

# 方法三：部分属性定位
# 1.当元素属性过长
# 2.元素属性值内容中存在动态变换的情况下  第一次打开 text="id_9" 第二次打开text="id_10" 第三次打开text="id_11"
print('hello'.startswith('he'))  # 查找以什么开头的字符串
# #  以什么开头
# driver.find_element(By.XPATH, '//android.widget.Button[end-with(@resource-id="digit_9")]').click()
#  包含某一个
driver.find_element(By.XPATH, '//android.widget.Button[contains(@resource-id,"digit_8")]').click()
#  以什么结尾
driver.find_element(By.XPATH, '//android.widget.Button[ends-with(@resource-id,"digit_9")]').click()
