from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

desired_caps={}
#平台类型
desired_caps['platformName'] = 'Android'
#平台版本号
desired_caps['platformVersion'] = '5.1'
#设备名称
desired_caps['deviceName'] = 'Android Emulator'
#app包名营销一体化pagename
desired_caps['appPackage'] = 'com.lanren.jz'
#app入口页面acitivity
desired_caps['appActivity'] = 'com.caiyi.accounting.jz.StartActivity'
#不重置
# desired_caps['noReset'] = True
#连接appium server 前提appium server要启动

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

#在运行代码之前1.appium server启动成功，处于监听状态
#2、模拟器和真机必须被电脑识别，


#id
# driver.find_element_by_id('')
# #class
# driver.find_elements_by_class_name('')
# #content-desc
# driver.find_element_by_accessibility_id('')
# #AndroidUiAutomator前三种不能唯一定位时使用
# driver.find_element_by_android_uiautomator('new UiSelector().text("请输入用户名或邮箱") ')
#和web区别是MobileBy.ID来By.id

#实现首页欢迎的滑动操作
size = driver.get_window_size()#获取窗口长宽
print(size)
start_x = size['width'] * 0.9
start_y = size['height'] * 0.5
end_x = size['width'] * 0.1
end_y = size['height'] * 0.5
driver.swipe(start_x,start_y,end_x,end_y)
import time
time.sleep(2)
driver.swipe(start_x,start_y,end_x,end_y)
#立即体验的坐标
TouchAction(driver).tap(x=int(size['width']*0.5),y=int(size['height']*0.9)).perform()


#点击我的
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,'com.lanren.jz:id/tab_text')))

driver.find_element_by_id('com.lanren.jz:id/tab_text').click()

#点击登录按钮
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,'com.lanren.jz:id/login_hint')))

#方法一
driver.find_element_by_id('com.lanren.jz:id/login_hint').click()
#方法二通过UISelector进行定位
# driver.find_element_by_android_uiautomator('new UiSelector().text("注册/登录")').click()

#输入用户名
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,'com.lanren.jz:id/et_phone')))
#点击用户名
driver.find_element_by_id('com.lanren.jz:id/et_phone').send_keys('18018039181')
#输入密码
driver.find_element_by_id('com.lanren.jz:id/et_pwd').send_keys('huahua1002')
#点击登录按钮
driver.find_element_by_id('com.lanren.jz:id/btn_login').click()