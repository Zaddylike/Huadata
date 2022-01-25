import requests, os, time, re, csv, pandas, json
from functools import wraps

from sqlalchemy import false
from APIparams import modelname_forAPI

def runtime(func):
    @wraps(func)
    def inner(*args,**kwargs):
        start = time.time()
        print('\033[96m'+time.strftime("RunStart: %h %d,%Y %H:%M:%S")+'\033[0m')

        func(*args,**kwargs)

        end = time.time()-start
        hours, rem = divmod(end-start, 3600)
        minutes, seconds = divmod(rem, 60)
        print('\033[96m'+time.strftime("RunEnd: %h %d,%Y %H:%M:%S")+"\nAll Test Run in {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds)+'\033[0m')
        
    return inner
#

def CheckLogExist():
    try:
        if os.path.exists(r'.\TPCR\AIKernel-Preprocessing_API_Log.csv'):
            pass
        else:
            raise
    except:
        with open('.\TPCR\AIKernel-Preprocessing_API_Log.csv','w',encoding='utf-8',newline="") as file:
            writer = csv.writer(file)
            writer.writerow(['API','Model Name','Response Code','Response Content','Response Time','Pass/Fail'])
#

class APIPattern:
    def __init__(self,data):
        self.url = data['request']["url"]
        self.header = data['request']['headers']
        self.method = data['request']['method']

        self.params = data['request']['params']
        self.data = data['request']['data']
        self.file = data['request']['file']

    def CheckMethod(self):
        if self.method.upper() == "GET":
            self.GetDataRes()
        elif self.method.upper() == "POST":
            self.PostFataRes()

    def GetDataRes(self):
        self.res=requests.get(
            self.url, 
            headers=self.header, 
            params=self.params, 
            )
        return self.res

    def PostDataRes(self):
        self.res=requests.post(
            self.url,
            headers=self.header, 
            params=self.params, 
            data=self.data,
            files=self.file
            )
        return self.res

    def ParserRes(self):
        print(self.res)
        
if __name__ == '__main__':

    with open('./paramspost.json','r',encoding='utf-8') as file:
        main = APIPattern(data=json.load(file))
        main.GetDataRes()
        res = main.PostDataRes()
        print(res.text)