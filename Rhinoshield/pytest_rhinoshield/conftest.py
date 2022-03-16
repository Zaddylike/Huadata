import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

import time,json

@pytest.fixture(params=["chrome"])
def browser_setup(request):
    if request.param == "chrome":
        options= webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # options.add_argument("--headless")
        service = Service('../chromedriver.exe')
        driver = webdriver.Chrome(service=service,options=options)
        # driver.get("https://rhinoshield.tw/")

        yield driver

        print("Test Completed")
        driver.close()
        driver.quit()
        
with open("person.json",'r',encoding="utf-8") as file:
        user = json.load(file)

@pytest.fixture(params=user)
def privadata(request):
    return request.param

@pytest.fixture(scope='function',autouse=True)
def takebreak():
    time.sleep(3)
