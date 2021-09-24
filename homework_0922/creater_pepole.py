# -*- coding: utf-8 -*-
# @Time : 2021/9/24 11:27
# @Author : Limusen
# @File : creater_pepole


import time
from appium import webdriver
from appium.webdriver.webdriver import By
import pytest
import random

des = {
    "platformName": "Android",
    "platformVersion": "8.1.0",
    "deviceName": "vivo x20",
    "appPackage": "com.android.contacts",
    "appActivity": "com.android.contacts.DialtactsContactsEntryActivity",
    "udid": "c6c8c4ce",
    "noReset": True,
    "newCommandTimeout": 30  # 30s没对手机发送新命令，就断开连接
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
driver.implicitly_wait(10)


def phone():
    number = ['130', '136', '138', '137', '150', '155', '158', '177', '186', '185']
    phone = random.choice(number) + "".join(random.choice('0123456789') for i in range(8))
    return phone


def name():
    name = ["赵", "钱", "孙", "李"]
    ming = random.choice(name) + "".join(random.choice("幸福家园") for i in range(2))
    return ming


if __name__ == '__main__':
    for i in range(1, 11):
        number = phone()
        Lname = name()
        time.sleep(1)
        driver.find_element(By.XPATH, '//android.widget.Button[@bounds="[936,72][1074,210]"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//android.widget.EditText[@text="姓名"]').send_keys(Lname)
        time.sleep(1)
        driver.find_element(By.XPATH, '//android.widget.EditText[@text="电话"]').send_keys(number)
        time.sleep(1)
        driver.find_element(By.XPATH, '//android.widget.Button[@text="完成"]').click()
    print("----over----")
