import requests, os, time, re, csv, pandas
from functools import wraps
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

class APIto_NY:
    def __init__(self,url,data,para):
        self.url = url
        self.params = para
        self.data = data
        self.header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
        }

    def ParamsCheck(self):
        if self.data.endswith('.txt',-4):
            self.param = {
                'model':self.params
            }
            self.data = [
                {
                    "fid": "1",
                    "data": open(self.data,'r').read()
                    }
                    ]
        else:
            self.param = {
                'model':self.params
            }
            self.data = {
                'data':open(self.data,'rb')
            }

    def GetDataRes(self):
        res = requests.get(
            self.url,
            headers = self.header,
            params = self.param,
            json = self.data
            )
        return res

    def PostDataRes(self):
        res = requests.post(
            self.u,
            headers = self.header,
            params = self.param,
            json = self.data
            )

        return res

    def ResStatus(self,res):
        if res.status_code == 201:
            print(f"Status Code:{res.status_code}")
            return 201
        else:
            return 422

    def PassorFail(self,res):
        if res.status_code == 201:
            return 'pass'
        else:
            return 'fail'

    def ParserRes(self,res):
        status = self.res_status(res)
        passorfail = self.check_result(res)

        res = res.json()
        response = [self.url,self.params,status,res['txt'],passorfail]
        with open('.\TPCR\AIKernel-Preprocessing_API_Log.csv','a',encoding='utf-8',newline="") as file:
            writer = csv.writer(file)
            writer.writerow(response)
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

if __name__ == '__main__':
    CheckLogExist()
    time=0
    while True:
        for i in modelname_forAPI:
            dicomfile = os.listdir(f'C:\\{i}')
            #目標網址、夾帶檔案、參數
            process =  APIto_NY('https://stag.ai.efai.tw/infer/b64/',f'.\\data\\{i}\\{dicomfile[0]}',i)
            process.ParamsCheck()
            res = process.PostDataRes()
            process.ParserRes(res)
        time+=1
        print(time)
        if int(time)==1000:
            break