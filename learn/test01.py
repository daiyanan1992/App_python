from appium import webdriver


desired_caps={}
#平台类型
desired_caps['platformName'] = 'Android'
#平台版本号
desired_caps['platformVersion'] = '5.1'
#设备名称
desired_caps['deviceName'] = 'Android Emulator'
#app包名营销一体化pagename
desired_caps['appPackage'] = 'com.marketing'
#app入口页面acitivity
desired_caps['appActivity'] = 'com.marketing.MainActivity'

desired_caps['automationName'] = 'UiAutomator1'




#连接appium server 前提appium server要启动

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

#在运行代码之前1.appium server启动成功，处于监听状态
#2、模拟器和真机必须被电脑识别，