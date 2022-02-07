from appium import webdriver
from appium.webdriver.common.mobileby import  MobileBy
from appium.webdriver.extensions.android.nativekey import AndroidKey
import time
import selenium
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
import sys
import cv2
sys.path.append("../")

class app():
    def __init__(self):
        print('selenium version = ', selenium.__version__)
        desired_caps = {
            'platformName':'Android',
            'platformVersion':'11.0',
            'deviceName':'first-0000',
            'noReset':"True",
            "resetKeyboard":"True"
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver=driver
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()["height"]
        self.x=x
        self.y=y

    def test_01(self):
        #into a app
        # print(self.x,self.y)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((MobileBy.ACCESSIBILITY_ID,'蝦皮購物'))).click()


    def test_02(self):
        #login account
        user='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[5]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView'
        login='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[4]'
        account='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.EditText'
        password='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.EditText'
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((MobileBy.XPATH,user))).click()
        time.sleep(0.8)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((MobileBy.XPATH,login))).click()
        time.sleep(0.8)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((MobileBy.XPATH,account)))
        self.driver.find_element(MobileBy.XPATH,account).send_keys("0900211510")
        time.sleep(0.8)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((MobileBy.XPATH,password)))
        self.driver.find_element(MobileBy.XPATH,password).send_keys("2Ukidding")
        time.sleep(0.8)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((MobileBy.ID,"com.shopee.tw:id/btnLogin"))).click()


    def test_03(self):
        #search field&search
        time.sleep(0.8)
        shp='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ImageView'
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((MobileBy.XPATH,shp))).click()
        time.sleep(0.8)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((MobileBy.ID,'com.shopee.tw:id/text_search'))).click()
        time.sleep(0.8)
        x='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText'
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((MobileBy.XPATH,x)))
        self.driver.find_element(MobileBy.XPATH,x).send_keys("iphone")
        self.driver.keyevent(keycode=66)


    def test_04(self):
        #setting x,y
        time.sleep(0.8)
        #refresh
        self.driver.swipe(int(1/2*self.x),int(2/8*self.y),int(1/2*self.x),int(7/8*self.y),duration=800)
        #filter
        self.driver.swipe(int(3/4*self.x),int(2/4*self.y),int(1/4*self.x),int(2/4*self.y))
        self.driver.swipe(int(1/4*self.x),int(2/4*self.y),int(3/4*self.x),int(2/4*self.y))


    def test_05(self):
        #into a product page
        x='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[6]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]'
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((MobileBy.XPATH,x))).click()

    
    def test_06(self):
        #swipe pic
        for i in range(2):
            time.sleep(0.8)
            self.driver.swipe(int(3/4*self.x),int(1/4*self.y),int(1/4*self.x),int(1/4*self.y))


    def test_07(self):
        for i in range(4):
            self.driver.swipe(int(1/2*self.x),int(5/8*self.y),int(1/2*self.x),int(1/8*self.y))


    def test_08(self):
        #buy button
        x='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup[4]'
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((MobileBy.XPATH,x))).click()


    def test_09(self):
        #select purchase-options
        style='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]'
        getbut='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup'
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((MobileBy.XPATH,style))).click()
        time.sleep(0.8)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((MobileBy.XPATH,getbut))).click()
        time.sleep(0.8)


    def test_10(self):
        #get back
        back='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ImageView'
        back1='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ImageView'
        back2='android.widget.ImageView'
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((MobileBy.XPATH,back))).click()
        time.sleep(0.8)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((MobileBy.XPATH,back1))).click()
        time.sleep(0.8)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((MobileBy.CLASS_NAME,back2))).click()
        time.sleep(0.8)


    def quit(self):
        #log out and quit
        user='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[5]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView'
        sett='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView'
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((MobileBy.XPATH,user))).click()
        time.sleep(0.8)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((MobileBy.XPATH,sett))).click()
        time.sleep(0.8)
        self.driver.swipe(int(1/2*self.x),int(6/8*self.y),int(1/2*self.x),int(3/8*self.y))
        time.sleep(0.8)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((MobileBy.ID,"com.shopee.tw:id/btnLogout"))).click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((MobileBy.ID,"com.shopee.tw:id/buttonDefaultPositive"))).click()
        self.driver.quit()


if __name__=="__main__":        
    shopped=app()
    shopped.test_01()
    shopped.test_02()
    shopped.test_03()
    shopped.test_04()
    shopped.test_05()
    shopped.test_06()
    shopped.test_07()
    shopped.test_08()
    shopped.test_09()
    shopped.test_10()
    shopped.quit()