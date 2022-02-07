#coding=utf-8
from appium import webdriver

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_phonenumber import numberinput

class APP_aiauto(numberinput):
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '11.0'
        desired_caps['deviceName'] = 'test-0001'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.keyevent(3)
        size= self.driver.get_window_size()
        print(size)
    def quitdriver(self):
        self.driver.keyevent(3)
        self.driver.quit()

if __name__ == "__main__":
    main = APP_aiauto()
    main.openapplist()
    main.phoneinput()
    main.addcontact()
    main.decontact()
    main.quitdriver()