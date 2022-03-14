from pydoc import classname
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import json,time
from bs4 import BeautifulSoup


'''
測試單元測試會先確認是否存在(使用顯性)再操作(click,snedkey..)。
'''


'''
BaseSetting :
    把Driver,method模組化,減少日後做重複工作,減少時間成本。
'''
class BaseSetting:
    def __init__(self):
        self._setting()
        self.driver = webdriver.Chrome(service=self.service,options=self.op)
        return self.driver

    def _setting(self):
        self.service = Service("../chromedriver.exe")
        self.op = webdriver.ChromeOptions()
        self.op.add_experimental_option('excludeSwitches', ['enable-logging'])
        # self.op.add_argument("--headless")
    '''
    cksome : 點擊
    sksome : 輸入
    selecttsome : 下拉式選單
    '''
    def cksome(self,xpath):
        WebDriverWait(self.driver,12,0.5).until(EC.visibility_of_element_located((By.XPATH,xpath)),f"No found {xpath}").click()
        time.sleep(0.5)
    def sksome(self,xpath,contents):
        WebDriverWait(self.driver,12,0.5).until(EC.visibility_of_element_located((By.XPATH,xpath)),f"No found {xpath}").send_keys(contents)
        time.sleep(0.5)
    def selectsome(self,xpath,indexORcontent):
        select = Select(self.driver.find_element(By.XPATH,xpath))
        try:
            select.select_by_index(indexORcontent)
        except:
            select.select_by_value(indexORcontent)
        time.sleep(0.5)


class rhino_user(BaseSetting):
    def __init__(self,url):
        self.url = url
        self.driver = super().__init__()

    '''
        登入
    '''
    def login(self):
        if self.driver.current_url != self.url:
            self.driver.get(self.url)
        #user page
        super().cksome('//*[@id="navigation-bar"]/div[2]/div/div[2]/div/div[2]')
        #input acc
        WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located((By.ID,'customer_email'))).send_keys(user['account'])
        #input pas
        WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located((By.ID,'customer_password'))).send_keys(user['password'])
        #click login button 
        super().cksome('//*[@id="customer_login"]/div/input')
        time.sleep(5)
        #back to userpage
        super().cksome('//*[@id="navigation-bar"]/div[2]/div/div[2]/div/div[2]')
        super().cksome('//*[@id="navigation-bar"]/div[2]/div/div[2]/div/div[2]')
        #check login success
        WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located((By.CLASS_NAME,"page__title")),"False")
    '''
        登出
    '''
    def logout(self):
        if self.driver.current_url != self.url:
            self.driver.get(self.url)
        #user page
        super().cksome('//*[@id="navigation-bar"]/div[2]/div/div[2]/div/div[2]')
        #click to logout button
        WebDriverWait(self.driver,8,0.5).until(EC.visibility_of_element_located((By.ID,'logout-button')),"Loging Error").click()
        #back to userpage
        super().cksome('//*[@id="navigation-bar"]/div[2]/div/div[2]/div/div[2]')
        #check logout success
        if WebDriverWait(self.driver,8,0.5).until(EC.visibility_of_element_located((By.ID,'customer_email'))):
            return "pass"
        else:
            return "false"
    '''
        選擇商品規格
    '''
    def select_form(self):
        if self.driver.current_url != self.url:
            self.driver.get(self.url)
        #點擊導覽列進去
        super().cksome('//*[@id="navigation-bar"]/div[2]/div/div[1]/div[3]/dl/dd[1]')
        #點擊品牌選單
        self.driver.find_element(By.ID,'apple').click()
        #點擊型號選單
        WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located((By.CLASS_NAME,"options-picker")),"Not found choose__title")
        WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located((By.ID,"iphone-13")),"Not found option").click()
        #點擊手機殼風格
        super().cksome('//*[@id="__layout"]/div/div[3]/div[2]/div/div[1]/div')
    '''
        選擇商品細節(顏色、數量...)
    '''
    def select_goodsdetail(self):
        super().cksome('//*[@id="mystic_green"]/div/input')
        super().selectsome('//*[@id="device-selector"]/select',3)
        super().cksome('//*[@id="__layout"]/div/div[3]/div[2]/div/div[3]/div/div/div/div[1]/section[2]/section[4]/div[3]/button')
        try:
            super().cksome('//*[@id="__layout"]/div/div[3]/div[2]/div/div[3]/div/div/div/div[1]/div[4]/section[2]/button')
        except:
            pass

    '''
        檢查購物車是否有貨，及其資訊是否正確
    '''
    def checkshopcart(self):
        WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located((By.CLASS_NAME,"navigation__functional__item")),"Not found option").click()
        WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located((By.ID,"CartProducts")),"Not found option")
        # self.driver.refresh()
        time.sleep(10)
        fullsoup = BeautifulSoup(self.driver.page_source,"html5lib")
        soup = fullsoup.find_all('div','tr')[1]
        print(soup.find('div','td title').text.strip())
        print(soup.find('div','td price').span.text.strip())

if __name__ == "__main__":
    with open("person.json",'r',encoding="utf-8") as file:
        user = json.load(file)
    main = rhino_user("https://rhinoshield.tw/")
    main.login()
    main.select_form()
    main.select_goodsdetail()
    main.checkshopcart()
    main.logout()