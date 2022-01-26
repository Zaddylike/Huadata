from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import requests
import time,datetime
import re
import os
import json

class WebTest:
    def __init__(self):
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
        self.driverPath = Service("./chromedriver.exe")
        self.opt = webdriver.ChromeOptions()
        self.opt.add_argument(f"user-agent={headers}")
        self.opt.add_argument('--headless')
        self.opt.add_experimental_option('excludeSwitches', ['enable-logging'])

    #init Selenium
    def Run(self,args):
        self.driver = webdriver.Chrome(service=self.driverPath, options=self.opt)
        self.driver.get(args)
        if self.driver:
            return True
        else:
            return False

    #stop Selenium
    def StopRun(self):
        self.driver.quit()

    #input
    def SearchSome(self,*args):
        element, keyword = args
        Search = self.driver.find_element(By.XPATH,element)
        Search.send_keys(keyword,Keys.ENTER)

    #click
    def ClickSome(self,args):
        element = args
        Click = self.driver.find_element(By.XPATH,element)
        Click.click()

    #get onday article
    def FindOnday(self,args):
        global times,res
        element = args
        for i in self.driver.find_elements(By.CLASS_NAME,element):
            if i.find_element(By.CLASS_NAME,'date').text != ProcessTime():
                times-=1
                if times==0:
                    return False
            else:
                self.SearchIP(i)
                res[0]['Total']+=1
                if res[0]['Total']==50:
                    self.StopRun()
                    return False
        NextUrl = i.find_element(By.XPATH,"//*[@id='action-bar-container']/div/div[2]/a[2]").get_attribute('href')
        self.StopRun()

        return NextUrl

    #get onday article ip
    def SearchIP(self,i):
        IP = self.PreProcess(i)
        print(f"第{res[0]['Total']}次搜尋,結果: {IP}")
        try:
            IPAddress = requests.get(f"http://api.ipapi.com/api/{IP}",params={"access_key":"fa7500daf99702a2c91e48a2dfc4f30f"})
        except:
            raise Exception("This IP Not Found")
        # IPAddress = re.split(r';',IPAddress)[3]
        self.SaveData(IPAddress.json())

    #process ip
    def PreProcess(self,i):
        Repattern = "來自: \d+\.\d+.\d+\.\d+"
        address = i.find_element(By.XPATH,'//*[@id="main-container"]/div[2]/div[2]/div[2]/a').get_attribute('href')
        Art = requests.get(address,cookies={"over18":"1"})
        match = re.search(Repattern, Art.text)
        match = re.split(" ",match.group())[1]

        return match

    #save res    
    def SaveData(self,address):
        global res
        try:
            if address['country_name'] not in res[1].keys():
                res[1][address['country_name']]=1
            else:
                res[1][address['country_name']]+=1
        except:
            raise Exception("Country Can't update res")
        try:
            if address['city'] not in res[2].keys():
                res[2][address['city']]=1
            else:
                res[2][address['city']]+=1
        except:
            raise Exception("City Can't update res")


def ProcessTime():
    todaY1=datetime.date.today()
    todaY2=str(todaY1).split("-")   
    if int(todaY2[1]) < 10:         
        todaY=" "+str(int(todaY2[1]))+"/"+todaY2[2]    
    else:   
        todaY=todaY2[1]+"/"+todaY2[2]

    return todaY.strip()

def CreateRes():
    res=[]
    res.append({"Total":0})
    res.append({})
    res.append({})
    return res


if __name__ == "__main__":
    print("搜尋測試設定為50次")
    main = WebTest()
    Url = r'https://www.ptt.cc/bbs/Gossiping/index.html'
    res = CreateRes()
    times = 10

    while Url:
        main.Run(Url)
        main.ClickSome('/html/body/div[2]/form/div[1]/button')
        Url = main.FindOnday('r-ent')
        if not Url:
            break


    with open('IPres.json','w+',encoding="utf-8") as writefile:
        json.dump(res, writefile, indent=4)
    print(f"total article: {res[0]['Total']}")
    for n,t in res[1].items():
        print(n,t)
    for n,t in res[2].items():
        print(n,t)
    



'''
from selenium import webdriver
## BY: 也就是依照條件尋找元素中XPATH、CLASS NAME、ID、CSS選擇器等都會用到的Library
from selenium.webdriver.common.by import By
## keys: 鍵盤相關的Library
from selenium.webdriver.common.keys import Keys
## Select: 下拉選單相關支援，但前端框架UI工具不適用(ex: Quasar、ElementUI、Bootstrap)
from selenium.webdriver.support.ui import Select
## WebDriverWait: 等待頁面加載完成的顯性等待機制Library
from selenium.webdriver.support.ui import WebDriverWait
## ActionChains: 滑鼠事件相關
from selenium.webdriver.common.action_chains import ActionChains
## expected_conditions: 條件相關
from selenium.webdriver.support import expected_conditions as EC
## BeautifulReport: 產生自動測試報告套件
from BeautifulReport import BeautifulReport
## Chrome WebDriver 需要DRIVER Manager的支援
from webdriver_manager.chrome import ChromeDriverManager
## 延遲時間相關
import time
## 單元測試模組，線性測試用不到
import unittest
'''