import time

from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC



class WebFunc:
    '''
    cksome : 點擊
    sksome : 輸入
    selecttsome : 下拉式選單
    '''

    def cksome(self,driver,xpath,error=""):
        WebDriverWait(driver,12,0.5).until(EC.visibility_of_element_located((By.XPATH,xpath)),f"No found {error}").click()
        time.sleep(0.5)
    def sksome(self,driver,xpath,contents,error):
        WebDriverWait(driver,12,0.5).until(EC.visibility_of_element_located((By.XPATH,xpath)),f"No found {error}").send_keys(contents)
        time.sleep(0.5)
    def selectsome(self,driver,xpath,indexORcontent):
        select = Select(driver.find_element(By.XPATH,xpath))
        try:
            select.select_by_index(indexORcontent)
        except:
            select.select_by_value(indexORcontent)
