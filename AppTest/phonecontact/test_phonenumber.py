#coding=utf-8
from http.client import TOO_MANY_REQUESTS
from appium import webdriver

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction



class numberinput:
    def checkandclick(self,element:str,att):
        if att == "aid":
            att = MobileBy.ACCESSIBILITY_ID
        elif att == "id":
            att = MobileBy.ID
        elif att == 'xpath':
            att = MobileBy.XPATH

        WebDriverWait(self.driver,8).until(EC.visibility_of_element_located((att,element)))
        self.driver.find_element(att,element).click()
    
    def checkandsendkeys(self,element:str,att,text:str):
        if att == 'xpath':
            att = MobileBy.XPATH

        WebDriverWait(self.driver,8).until(EC.visibility_of_element_located((att,element)))
        self.driver.find_element(att,element).send_keys(text)

    def clickanddraw(self,element:str,att):
        if att == "aid":
            att = MobileBy.ACCESSIBILITY_ID
        elif att == "id":
            att = MobileBy.ID
        elif att == 'xpath':
            att = MobileBy.XPATH

        WebDriverWait(self.driver,8).until(EC.visibility_of_element_located((att,element)))
        action = TouchAction(self.driver)
        action.long_press(x=20,y=1688,duration=2).move_to(x=20,y=500).release().perform()


    def openapplist(self):
        self.clickanddraw('com.google.android.apps.nexuslauncher:id/page_indicator','id')
    def phoneinput(self):
        try:
            self.checkandclick("Phone","aid")
            self.checkandclick("com.android.dialer:id/call_log_tab",'id')
            self.checkandclick("com.android.dialer:id/empty_list_view_action",'id')
            from numberlist import number
            for i in number:
                self.checkandclick(i,'aid')
            for i in range(3):
                self.checkandclick('backspace','aid')
            return True
        except:
            raise Exception("input error")

    def addcontact(self):
        try:
            self.checkandclick('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView','xpath')
            self.checkandsendkeys("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]","xpath","watson")
            self.checkandsendkeys("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[2]","xpath","liou")
            self.checkandclick('com.android.contacts:id/editor_menu_save_button','id')
            return True
        except:
            return False
    def decontact(self):
        try:
            self.checkandclick('More options','aid')
            self.checkandclick('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout','xpath')
            self.checkandclick('android:id/button1','id')
        except:
            return False

