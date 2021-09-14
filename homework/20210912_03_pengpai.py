# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 8:01 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : 20210912_01_setting.py
# @Software: PyCharm
# @desc :


import time
from appium import webdriver
from appium.webdriver.webdriver import By

des = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "mac虚拟机",
    "appPackage": "com.wondertek.paper",
    "appActivity": "cn.thepaper.paper.ui.main.MainActivity",
    "udid": "192.168.56.104:5555",
    "noReset": "True"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)

driver.find_element(By.XPATH, '//android.widget.ImageView[@bounds="[1217,2628][1329,2730]"]').click()

time.sleep(1)

driver.find_element(By.XPATH, '//android.widget.Button[@text="一键登录注册"]').click()

time.sleep(1)

driver.find_element(By.XPATH, '//android.widget.EditText[@text="输入11位手机号"]').send_keys("15574933885")

driver.find_element(By.XPATH,
                    '//android.widget.TextView[@resource-id="com.wondertek.paper:id/get_verification_code"]').click()

time.sleep(1)

driver.find_element(By.XPATH,
                    '//android.widget.CheckBox[@resource-id="com.wondertek.paper:id/checkbox_agreement"]').click()
