import requests, os, time, re, csv, pandas

from APIparams import modelname_forAPI



class APIto_NY:
    def __init__(self,u,dicomdata,para):
        self.u = u
        self.para = para
        self.dicomdata = dicomdata

        self.header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
        }

    def paracheck(self):
        if self.dicomdata.endswith('.txt',-4):
            self.param = {
                'model':self.para
            }
            self.data = [
                {
                    "fid": "1",
                    "data": open(self.dicomdata,'r').read()
                    }
                    ]
        else:
            self.param = {
                'model':self.para
            }
            self.data = {
                'data':open(self.dicomdata,'rb')
            }

    def getdata_res(self):
        RunNeed.RunTime('runstart')
        res = requests.get(
            self.u,
            headers = self.header,
            params = self.param,
            json = self.data
            )
        self.time = RunNeed.RunTime('runend')
    def postdata_res(self):

        RunNeed.RunTime('runstart')
        res = requests.post(
            self.u,
            headers = self.header,
            params = self.param,
            json = self.data
            )
        self.time = RunNeed.RunTime('runend')

        return (res)

    def call_back(self):
        print(f'API:{self.u}')
        print(f'ModelName:{self.para}')

    def res_status(self,res):
        if res.status_code == 201:
            print(f"Status Code:{res.status_code}")
            return 201
        else:
            return 422

    def check_result(self,res):
        if res.status_code == 201:
            return 'pass'
        else:
            return 'fail'

    def res_parser(self,res):
        self.call_back()

        status = self.res_status(res)
        passorfail = self.check_result(res)
        res = res.json()

        response = [self.u,self.para,status,res['txt'],self.time,passorfail]
        with open('.\TPCR\AIKernel-Preprocessing_API_Log.csv','a',encoding='utf-8',newline="") as file:
            writer = csv.writer(file)
            writer.writerow(response)


class RunNeed():
    @staticmethod
    def RunTime(t=None): #start from 1970s.1.1 than input start or end to run this function
        try:
            if t=="runstart":
                global start
                start = time.time()
                print('\033[96m'+time.strftime("RunStart: %h %d,%Y %H:%M:%S")+'\033[0m')
            elif t=="runend":
                end = time.time()
                hours, rem = divmod(end-start, 3600)
                minutes, seconds = divmod(rem, 60)
                print('\033[96m'+time.strftime("RunEnd: %h %d,%Y %H:%M:%S")+"\nAll Test Run in {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds)+'\033[0m')
                return "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds)
            else:
                raise
        except:
            print("errorInput")


def checklogexist():
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
    checklogexist()
    t=0
    RunNeed.RunTime('runstart')
    while True:
        for i in modelname_forAPI:
            dicomfile = os.listdir(f'C:\\Users\\EF-USER\\ProJect\\Portfolios\\Autumation Test\\ApiTest\\Aikermel\\AIKernel-PreprocessingAPI\\data\\{i}')
            if dicomfile[0].endswith('.txt',-4):
                #目標網址、夾帶檔案、參數
                process =  APIto_NY('https://stag.ai.efai.tw/infer/b64/',f'.\\data\\{i}\\{dicomfile[0]}',i)
                process.paracheck()
                res = process.postdata_res()
                process.res_parser(res)
            else:
                process =  APIto_NY('https://stag.ai.efai.tw/infer/file/',f'.\\data\\{i}\\{dicomfile[0]}',i)
                process.paracheck()
                res = process.postfile_res()
                process.res_parser(res)
            print()
        t+=1
        print(t)
        if int(t)==1000:
            break
    RunNeed.RunTime('runend')
    print("test done")






'''
        res=os.popen("curl -X 'POST' 'http://rdapi.efaipd.com/infer/file/?model=boneage' -H 'accept: application/json' -H 'Content-Type: multipart/form-data' -F 'data=@'"+datan)
'''