# -*- coding: utf-8 -*-
# @Time : 2021/9/7 17:55
# @Author : Limusen
# @File : demo2


from appium import webdriver

des = {
    "automationName": "Appium",  # 默认是配置appium
    "platformName": "Android",  # 平台名称 ios/android/firefox Os
    "platformVersion": "8.1.0",  # 安卓的版本
    "deviceName": "vivo x20",  # 随便填 没关系
    "app": r"D:\apk\jisuanqi.apk",
    "appPackage": "rock.Simple.Calculator",  # 包名
    "appActivity": "rock.Simple.Calculator.MainActivity",  # 活动入口
    "udid": "c6c8c4ce",  # adb连接的设备名称
    "noSign": True,
    "newCommandTimeout": 30  # 30s没对手机发送新命令，就断开连接
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)

# driver.find_element_by_xpath('//android.widget.LinearLayout/android.widget.FrameLayout/'
#                              'android.widget.LinearLayout/android.widget.LinearLayout[2]/'
#                              'android.widget.LinearLayout[2]/android.widget.Button[2]').click()

# # 使用text属性定位  '//属性值[@text=""]'
# driver.find_element_by_xpath('//android.widget.Button[@text="+"]').click()  # 点击＋号
# # 使用resource-id  '//属性值[@resource-id=""]'
# driver.find_element_by_xpath('//android.widget.Button[@resource-id="rock.Simple.Calculator:id/six_btn"]').click()  # 点击6
# # 使用bounds
# driver.find_element_by_xpath('//android.widget.Button[@bounds="[807,1458][1029,1958]"]').click()  # 点击=


# # 以什么元素开头    '//类名[contains(@元素名,"内容")]'  这里没有元素好定位的
# driver.find_element_by_xpath('//android.widget.Button[contains(@元素,"xxxxx")]').click()
# # 元素包含某某内容   '//类名[contains(@元素名,"内容")]'
# driver.find_element_by_xpath('//android.widget.Button[contains(@resource-id,"six_btn")]').click()
# # 末尾开始匹配   '//类名[ends-with(@元素名,"内容")]'
# driver.find_element_by_xpath('//android.widget.Button[ends-with(@resource-id,"one_btn")]').click()


# 点击 9
driver.find_element_by_android_uiautomator('text("9")').click()

# 点击9 新建一个UiSelect对象
driver.find_element_by_android_uiautomator('resourceId("rock.Simple.Calculator:id/nine_btn") ').click()

driver.find_element_by_android_uiautomator('new UiSelector().resourceId("rock.Simple.Calculator:id/eight_btn")').click()