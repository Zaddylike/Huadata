import pyautogui as pat
import cv2
import time
import random
import os
import csv
loginpas="efai2021"
idlist=["efai7854","efai2761","efai202e","efai2021","efai1258","efai5845","efai4552","efai6999"]
namelist=["name6542","name4658","name2021","name1258","name5845","name4552","name6999"]
numlist=["num32135","num2021","num1258","num5845","num4552","num6999"]

def minimize():
    find_pic("-.png",0.9,1)
def find_pic(picname,confiden,ti):
    result = pat.locateCenterOnScreen(picname, confidence=confiden)
    if result==None: 
        return "0"
    else:
        if ti>0:
            pat.click(result,clicks=ti)
        else:
            None

def find_pic_t(picname,confiden,ti):
    result = pat.locateCenterOnScreen(picname, confidence=confiden)
    if result==None: 
        return "0"
    else:
        if ti>0:
            pat.press("tab",presses=ti)
        else:
            None
def find_pic_d(picname,confiden,ti):
    result = pat.locateCenterOnScreen(picname, confidence=confiden)
    if result==None: 
        return "0"
    else:
        if ti>0:
            pat.press("down",presses=ti)
        else:
            None

def field_occupy():
    pat.keyDown("shift")
    pat.press("home")
    pat.press("delete")
    pat.keyUp("shift")
def random_sex_select():
    x=random.randint(1,10)
    return x

def input_text(text):
    pat.typewrite(text)
def backspace(p):
    pat.click(p)
    pat.keyDown("shift")
    pat.press("home")
    pat.keyUp("shift")
    pat.press("backspace")

def random_options_list():
    num=random.randint(3,6) #select number limit
    optionselect=random.sample([0,1,2,3,4,5],k=num) #random select number
    print("select num:",num)
    return optionselect
def random_file():
    x=random.randint(1,20)
    return x
def random_input():
    text=random.randint(10,(1,2,3,4,5,6,7,8,9,0))
def openexe():
    if find_pic("stemipic.png",0.5,2) != "0":       #程式點擊狀況
        print("Exe Success")
    else:
        print("Error Not Found PIc")



    if find_pic("Loginfield.png",0.5,1) != "0":     #輸入界面狀況
        print("Login Field Success")
    else:
        time.sleep(3)
        if find_pic("Loginfield.png",0.5,1) != "0":
            print("Login Field Success")
        else:
            print("Login Field Fail")



    if find_pic("passwordinput.png",0.5,1) != "0":  #輸入欄狀況
        print("Password Field Available")                       
        input_text(loginpas)                             #輸入密碼
    else:
        time.sleep(2)
        if find_pic("passwordinput.png",0.5,1) != "0":
            print("Password Field Available")                       
            input_text(loginpas)
        else:                   
            print("Password Field Fail")                    
    


    if find_pic("alreadyinput.png",0.7,1) !="0":    #輸入狀況
        print("Input Password Success")
    else:
        time.sleep(2)
        if find_pic("alreadyinput.png",0.7,1) !="0":
            print("Input Password Success")
        else:
            print("Input Password fail")



    if find_pic("loginok.png",0.5,2) != "0":
        print("LoginOK Success")                    #登入按鈕確認狀況
    else:
        time.sleep(2)
        if find_pic("loginok.png",0.5,2) != "0":
            print("LoginOK Success")
        else:
            print("LoginOK Fail")



    if find_pic("display.png",0.7,0) != "0":          #進入應用程式頁面狀況
        print("Login Success")
    else:
        time.sleep(2)
        if find_pic("display.png",0.7,0) != "0":
            print("Login Success")
        else:
            print("Login Fail")

def IDinput(): 
    if find_pic("IDfield.png",0.7,1) != "0":    #確認輸入病例號欄為empty
        print("Input IDfield Available-1")
        pat.moveRel(250,0)
        backspace(pat.position())
        if find_pic("ID patient wfield.png",0.5,0) != "0":  
            input_text(idlist[random.randint(1,7)])
            print("Input IDfield Success-1")
        else:
            print("Input IDfield Fail-1")
    else:
        time.sleep(2)
        if find_pic("IDfield.png",0.7,1) != "0":    #確認輸入病例號欄為empty
            print("Input IDfield Available-1")
            pat.moveRel(250,0)
            pat.click(pat.position())
            pat.press("backspace")
            if find_pic("ID patient wfield.png",0.5,0) != "0":  
                input_text(idlist[random.randint(1,7)])
                print("Input IDfield Success-1")
            else:
                print("Input IDfield Fail-1")

def Nameinput():
    if find_pic_t("Name field.png",0.5,1) !="0":    #確認輸入姓名欄為empty
        print("Input Namefield Available")
        input_text(namelist[random.randint(1,6)])
        if find_pic("Nameoccupy.png",0.5,0) != "0":
            print("Input Namefield Success")
        else:
            print("Input Namefield Fail")
    else:
        time.sleep(2)
        if find_pic_t("Nameoccupy.png",0.5,1) !="0":
            pat.press("backspace")
        if find_pic_t("Name field.png",0.5,1) !="0":
            input_text(namelist[random.randint(1,6)])
            if find_pic("Nameoccupy.png",0.5,0) != "0":
                print("Input Namefield Success")
            else:
                print("Input Namefield Fail")


def Numberinput():
    if find_pic_t("Number field.png",0.5,1) !="0":    #確認輸入Number欄為empty
        input_text(numlist[random.randint(1,5)])
        print("Input Numberfield Available")
        if find_pic("Numoccupy.png",0.5,0) !="0":    #確認輸入Number欄狀況有value
            print("Input Numberfield Success")
        else:
            print("Input Numberfield Fail")
    else:
        time.sleep(2)                                   #如果沒有確認到欄位座標 給予2秒反應時間後再次執行
        if find_pic_t("Numoccupy.png",0.5,1) !="0":
            pat.press("backspace")       
        if find_pic_t("Number field.png",0.5,1) !="0": 
            input_text(numlist[random.randint(1,6)])
            print("Input IDField Available")
            if find_pic("Numoccupy.png",0.5,0) !="0":    
                print("Input Numberfield Success")
        else:
            print("Input Numberfield Fail")



def age():
    if find_pic_t("ageinput.png",0.5,1) != "0":        #確認輸入age欄為empty
        print("Age Field Available")
        pat.press("backspace")
        if find_pic("ageinputempty.png",0.5,0) != "0":
            input_text("37")
            if find_pic("ageinput.png",0.5,0) != "0":      #確認age欄有value
                print("Input Age field Succcess")
            else:
                print("Input Age field Fail")          
    else:
        time.sleep(2)
        if find_pic_t("ageinput.png",0.5,1) != "0":  #如果沒有確認到欄位座標 給予2秒反應時間後再次執行
            print("Age Field Available")
            pat.press("backspace")
            if find_pic("ageinputempty.png",0.5,0) != "0":
                input_text("37")
                if find_pic("ageinput.png",0.5,0) != "0":   
                    print("Input Age field Succcess")
                else:
                    print("Input Age field Fail")          
        
def sex():
    if find_pic_t("man.png",0.7,1) != "0":
        print("Sex field Available")
        if random_sex_select() < int(5):
            if find_pic("female.png",0.5,1) !="0":
                print("Input Sex field Success")
        else:
            pass
            print("Input Sex field Success")
def options():
    optionselect1 = random_options_list()
    for j in range(6):
        if find_pic("go.png",0.8,1) != "0":
            print("op1clear")
        else:
            pass
    if find_pic("emptyoptions.png",0.5,0) != "0":
        print("options:",optionselect1)
        for i in optionselect1:
            if find_pic("op"+str(i)+".png",0.8,1) != "0":           #選取此次測試選項
                print("op"+str(i)+" has selected")
                time.sleep(0.5) 
def ASAP():
    if find_pic("asap.png",0.7,1) !="0":
        print("ASAPBTN Available")
        time.sleep(1)
        if find_pic("uploadfile.png",0.7,0) !="0":
            print("ASAPBTN Success")
            print()
        else:
            print("ASAPBTN Fail")
    else:
        time.sleep(2)
        if find_pic("asap.png",0.7,1) !="0":
            print("ASAPBTN Available")
            print()
            if find_pic("uploadfile.png",0.7,0) !="0":
                print("ASAPBTN Seccess")
                print()
            else:
                print("ASAPBTN Fail")
def Browse():
    if find_pic("browse.png",0.7,1) !="0":
        print("Browse Available")
        if find_pic("path.png",0.7,0) !="0":
            print("Browse Success")
        else:
            print("Browse Fail")
    else:
        time.sleep(2)
        if find_pic("browse.png",0.7,1) !="0":
            print("Browse Available")
            if find_pic("path.png",0.7,0) !="0":
                print("Browse Success")
            else:
                print("Browse Fail")
        else:
            print("Browse Fail")
def path_1():
    if find_pic("workpath.png",0.9,2) !="0":
        print("path_1 Available")
        if find_pic("stemi.png",0.9,0) !="0":
            print("path_1 Success")
        else:
            print("path_1 Fail")
    else:
        time.sleep(2)
        if find_pic("workpath.png",0.9,2) !="0":
            print("path_1 Available")
            if find_pic("stemi.png",0.9,0) !="0":
                print("path_1 Success")
            else:
                print("path_1 Fail")
        else:
            print("path_1 Fail")

def path_2():
    if find_pic("stemi.png",0.9,2) !="0":
        print("path_2 Available")
        if find_pic("testset.png",0.9,0) !="0":
            print("path_2 Success")
        else:
            print("path_2 Fail")
    else:
        time.sleep(2)
        if find_pic("stemi.png",0.9,2) !="0":
            print("path_2 Available")
            if find_pic("testset.png",0.9,0) !="0":
                print("path_2 Success")
            else:
                print("path_2 Fail")
        else:
            print("path_2 Fail")
def path_3():
    if find_pic("testset.png",0.9,2) !="0":
        print("path_3 Available")
        if find_pic("filelist.png",0.9,0) !="0":
            print("path_3 Success")
        else:
            print("path_3 Fail")
    else:
        time.sleep(2)
        if find_pic("testset.png",0.9,2) !="0":
            print("path_3 Available")
            if find_pic("filelist.png",0.9,0) !="0":
                print("path_3 Success")
            else:
                print("path_3 Fail")
        else:
            print("path_3 Fail")
def select_file():
    x=int(random_file())
    if find_pic_d("filelist.png",0.9,x) !="0":
        print("Select File Available")
        pat.press("enter")
        if find_pic("uploadfile.png",0.9,0) =="0":
            print("Select File Success")
        else:
            print("Select File Fail")
    else:
        time.sleep(2)
        if find_pic_d("filelist.png",0.9,x) !="0":
            print("Select File Available")
            pat.press("enter")
            if find_pic("uploadfile.png",0.9,0) =="0":
                print("Select File Success")
            else:
                print("Select File Fail")
        else:
            print("Select File Fail")
def final_OK():
    if find_pic("OK.png",0.9,1) !="0":
        print("finishtest Available")
        if find_pic("uploadfile.png",0.9,0) =="0":
            print("finishtest Success")
        else:
            print("finishtest Fail")
    else:
        time.sleep(2)
        if find_pic("OK.png",0.9,1) !="0":
            print("finishtest Available")
            if find_pic("filelist.png",0.9,0) =="0":
                print("finishtest Success")
            else:
                print("finishtest Fail")
        else:
            print("finishtest Fail")
def timecount():
    global testtime
    testtime+=1
    print(testtime)
        
def main():
    IDinput()
    Nameinput()
    Numberinput()
    age()
    sex()
    options()
    ASAP()
    Browse()
    path_1()
    path_2()
    path_3()
    select_file()
    final_OK()
    timecount()
    time.sleep(5)

    

testtime=0
if __name__ ==  "__main__":
    time.sleep(2)
    minimize()
    openexe()
    while True:
        main()




