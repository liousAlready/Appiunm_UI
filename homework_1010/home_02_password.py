# -*- coding: utf-8 -*-
# @Time : 2021/10/13 13:37
# @Author : Limusen
# @File : home_02_lock

import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import By

des = {
    "platformName": "Android",
    "platformVersion": "8.1.0",
    "deviceName": "vivox20",
    "appPackage": "com.android.settings",
    "appActivity": "com.android.settings.Settings",
    "udid": "c6c8c4ce",
    "noReset": "True"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
driver.implicitly_wait(10)

element_01 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="游戏模式"]')
element_02 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="飞行模式"]')

driver.scroll(element_01, element_02)
time.sleep(2)
driver.find_element(By.XPATH, '//android.widget.TextView[@text="指纹、面部与密码"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//android.widget.Button[@text="开启锁屏密码"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//android.widget.Button[@text="密码选项"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//android.widget.TextView[@text="图案密码"]').click()
time.sleep(2)
touch = TouchAction(driver)
touch.press(x=260, y=900).wait(1000).move_to(x=537, y=1450).wait(1000).move_to(x=813, y=1203).wait(1000).move_to(x=520,
                                                                                                           y=910).wait(
    1000).move_to(x=536, y=1207).wait(1000).release().perform()
time.sleep(2)
driver.save_screenshot("./password_press.png")