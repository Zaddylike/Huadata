import pytest,json,time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from .offtenfunc_web import WebFunc

with open("person.json",'r',encoding="utf-8") as file:
        user = json.load(file)

class Test_other(WebFunc):
    def test_other(self,privadata):
        print(privadata)

class Test_(WebFunc):
    def test_00(self,browser_setup):
        global driver
        driver = browser_setup
        driver.get('https://rhinoshield.tw/')
        assert "犀牛盾｜官方網站 – 犀牛盾 RhinoShield" in driver.title

    def test_login_01(self,privadata):
        super().cksome(driver,'//*[@id="navigation-bar"]/div[2]/div/div[2]/div/div[2]',"Not found 1-1")
        WebDriverWait(driver,12,0.5).until(EC.visibility_of_element_located((By.ID,'customer_email')),f"Not found 1-2").send_keys(privadata['account'])
        WebDriverWait(driver,12,0.5).until(EC.visibility_of_element_located((By.ID,'customer_password')),f"Not found 1-3").send_keys(privadata['password'])
        super().cksome(driver,'//*[@id="customer_login"]/div/input')
    
    def test_selectform_02(self):
        WebDriverWait(driver,12,0.5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="navigation-bar"]/div[2]/div/div[1]/div[3]/dl/dd[1]')),f"Not found 2-1").click()
        WebDriverWait(driver,12,0.5).until(EC.visibility_of_element_located((By.ID,'apple')),f"Not found 2-2").click()
        WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((By.CLASS_NAME,"options-picker")),"Not Found 2-3")
        WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((By.ID,"iphone-13")),"Not found 2-3").click()
        WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="__layout"]/div/div[3]/div[2]/div/div[1]/div')),"Not found 2-4").click()
    
    def test_goodsdetail_03(self):
        WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="mystic_green"]/div/input')),"Not found 3-1").click()
        Select(driver.find_element(By.XPATH,'//*[@id="device-selector"]/select')).select_by_index(3)
        WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="__layout"]/div/div[3]/div[2]/div/div[3]/div/div/div/div[1]/section[2]/section[4]/div[3]/button')),"Not found 3-2").click()
        try:
            WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="__layout"]/div/div[3]/div[2]/div/div[3]/div/div/div/div[1]/div[4]/section[2]/button')),"Not found 3-3").click()
        except:
            pass
    
    def test_checkcart_04(self):
        WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((By.CLASS_NAME,"navigation__functional__item")),"Not found 4-1").click()
        WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((By.ID,"CartProducts")),"Not found 4-2")
        time.sleep(3)
        fullsoup = BeautifulSoup(driver.page_source,"html5lib")
        soup = fullsoup.find_all('div','tr')[1]
        assert soup.find('div','td title').text.strip() == "iPhone 13 Pro Max 犀牛盾Clear透明手機殼"
        assert soup.find('div','td price').span.text.strip() == "$1,020 TWD" 

        # print(soup.find('div','td title').text.strip())
        # print(soup.find('div','td price').span.text.strip())

    def test_logout_05(self):
        super().cksome('//*[@id="navigation-bar"]/div[2]/div/div[2]/div/div[2]',"Not found 5-1")
        #click to logout button
        WebDriverWait(driver,8,0.5).until(EC.visibility_of_element_located((By.ID,'logout-button')),"Not found 5-2").click()
        #back to userpage
        super().cksome('//*[@id="navigation-bar"]/div[2]/div/div[2]/div/div[2]',"Not found 5-3")
        #check logout success
        if WebDriverWait(driver,8,0.5).until(EC.visibility_of_element_located((By.ID,'customer_email'))):
            return "pass"
        else:
            return "false"
