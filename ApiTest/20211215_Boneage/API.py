#coding=utf-8
import json,csv,time,sys,requests
sys.path.append("../")
from HuaFunc.OftenUsedFunc import CreateSomething, RunNeed
def Rt(func):
    def wrapper(url):
        print("\n\n\n")
        RunNeed.RunTime(t='start')
        func(url)
        RunNeed.RunTime(t='end')
    return wrapper
class api_test(object):
    def __init__(self,ModelID):
        with open("./para.json","r",encoding="utf8") as file:
            readfile=json.load(file)
        para=readfile
        self.para=para['beta']
        self.ModelID=ModelID
        with open(f'./base64file/{self.ModelID}/{self.ModelID}.txt','r',encoding='utf8') as file:
            base64file=file.read()
        self.base64file=base64file
    def Api_SC_Check(self,Respondata,apiname,i,t):
        if Respondata.status_code==self.para[apiname]['except']["status_code"]:
            print(f"Status Code: OK {Respondata.status_code}")
            with open("apilog.csv","a",newline="",encoding="utf8") as file:
                writer=csv.writer(file)
                writer.writerow([time.ctime(),apiname,Respondata.status_code,"PASS"])
            return Respondata.json()
        else:
            if self.para[apiname]["para"]['x-token'][i] in self.para[apiname]["para"]['x-token']:
                print("Incorrect Input:",self.para[apiname]["para"]['x-token'][i])
            else:
                r=Respondata.json()
                print("*********************************************")
                print(time.ctime())
                print(f"{apiname}: Status ERROR {Respondata.status_code}")
                print(f"{apiname}:{r['error']}")
                with open("apilog.csv","a",newline="",encoding="utf8") as file:
                    writer=csv.writer(file)
                    writer.writerow([time.ctime(),apiname,Respondata.status_code,r['error']])
                qua=input("wanna continue?(enter or 0)")
                if qua=="0":
                    quit()
                else:
                    pass
    @Rt
    def Api_Get_Token(self):
        print(f"ApiName: {'AT'}")
        for i in range(6):
            Respondata=requests.post(
                self.para["AT"]["url"],
                headers={
                    'x-api-key':self.para['AT']["para"]['x-token'][i].encode("utf-8").decode("latin1")
                    }
                )
            try:
                token=self.Api_SC_Check(Respondata,'AT',i,t)
                self.token=token["result"]['token']
                print(f"Result:{self.token}")
            except:
                print(f"Result:{token}")
    @Rt
    def Api_GET_Models(self):
        print(f"ApiName: {'AI'}")
        self.para["AI"]['para']['x-token'].insert(0,self.token)
        for i in range(6):
            Respondata=requests.get(
                self.para["AI"]['url'],
                headers={
                    "x-token":self.para["AI"]['para']['x-token'][i].encode("utf-8").decode("latin1")
                    }
                )
            try:
                modelid=self.Api_SC_Check(Respondata,'AI',i,t)
                print(f"Result:{modelid['result']}")
            except:
                print(f"Result:{modelid}")
    @Rt
    def Api_Make_Inference(self):
        print(f"ApiName: {'MI'}")
        self.para["MI"]['para']['x-token'].insert(0,self.token)
        for i in  range(6):
            Respondata=requests.post(
                self.para["MI"]['url'],
                headers={
                    "x-token":self.para["MI"]["para"]['x-token'][i].encode("utf-8").decode("latin1")
                    },
                data={
                    'model_id':self.ModelID,
                    'image':self.base64file
                    }
                )
            try:
                InferID=self.Api_SC_Check(Respondata,"MI",i,t)
                self.InferID=InferID['result']['infer_id']
                print(f"Result:{self.InferID}")
            except:
                print(f"Result:{InferID}")
    @Rt
    def Api_Make_Inference_Incorrectmodelid(self):
        print(f"ApiName: {'MI-ERROR1'}")
        for i in  range(6):
            Respondata=requests.post(
                self.para["MI"]['url'],
                headers={
                    "x-token":self.token
                    },
                data={
                    'model_id':self.para["MI"]["para"]['x-token'][i],
                    'image':self.base64file
                    }
                )
            try:
                InferID=self.Api_SC_Check(Respondata,'MI',i,t)
                self.InferID=InferID['result']['infer_id']
                print(f"Result:{self.InferID}")
            except:
                print(f"Result:{InferID}")
    @Rt
    def Api_Make_Inference_IncorrectBase64(self):
        print(f"ApiName: {'MI-ERROR2'}")
        for i in  range(6):
            Respondata=requests.post(
                self.para["MI"]['url'],
                headers={
                    "x-token":self.token
                    },
                data={
                    'model_id':self.ModelID,
                    'image':self.para["MI"]['para']['x-token'][i]
                    }
                )
            try:
                InferID=self.Api_SC_Check(Respondata,'MI',i,t)
                self.InferID=InferID['result']['infer_id']
                if self.InferID==None:
                    pass
                else:
                    print(f"Result:{self.InferID}")
            except:
                print(f"Result:{InferID}")
    @Rt
    def Api_GET_Inference(self):
        print(f"ApiName: {'GI'}")
        self.para["GI"]['para']['x-token'].insert(0,self.token)
        for i in range(6):
            Respondata=requests.get(
                self.para["GI"]['url'],
                headers={
                    "x-token":self.para["GI"]['para']['x-token'][i].encode("utf-8").decode("latin1")
                    },
                params={
                    'infer_id':self.InferID
                    }
                )
            try:
                Result=self.Api_SC_Check(Respondata,'GI',i,t)
                self.Result=Result['result']['txt']
                print(f"Result:{self.Result}")
            except:
                print(f"Result:{Result}")
    @Rt
    def Api_GET_Inference_Incorrectinferid(self):
        print(f"ApiName: {'GI-ERROR1'}")
        for i in range(6):
            Respondata=requests.get(
                self.para["GI"]['url'],
                headers={
                    "x-token":self.token
                    },
                params={
                    'infer_id':self.para["GI"]['para']['x-token'][i].encode("utf-8").decode("latin1")
                    }
                )
            try:
                Result=self.Api_SC_Check(Respondata,'GI',i,t)
                self.Result=Result['result']['txt']
                print(f"Result:{self.Result}")
            except:
                print(f"Result:{Result}")
    @Rt
    def Api_GET_PDF_Inference(self):
        print(f"ApiName: {'GPI'}")
        self.para["GPI"]['para']['x-token'].insert(0,self.token)
        for i in range(6):
            Respondata=requests.get(
                self.para["GPI"]['url'],
                headers={
                    "x-token":self.para["GPI"]['para']['x-token'][i].encode("utf-8").decode("latin1")
                    },
                params={
                    'infer_id':self.InferID
                    }
                )
            try:
                Result=self.Api_SC_Check(Respondata,'GI',i,t)
                self.Result=Result['result']['file']
                print(f"Result:{self.Result}")
            except:
                print(f"Result:{Result}")
    @Rt    
    def Api_GET_PDF_Inference_Incorrectinferid(self):
        print(f"ApiName: {'GPI-ERROR1'}")
        for i in range(6):
            Respondata=requests.get(
                self.para["GI"]['url'],
                headers={
                    "x-token":self.token
                    },
                params={
                    'infer_id':self.para["GPI"]['para']['x-token'][i].encode("utf-8").decode("latin1")
                    }
                )
            try:
                Result=self.Api_SC_Check(Respondata,'GI',i,t)
                self.Result=Result['result']['file']
                print(f"Result:{self.Result}")
            except:
                print(f"Result:{Result}")
    @Rt
    def Api_GET_Balance(self):
        print(f"ApiName: {'GB'}")
        self.para["GB"]['para']['x-token'].insert(0,self.token)
        for i in range(6):
            Respondata=requests.get(
                self.para["GB"]['url'],
                headers={
                    "x-token":self.para["GB"]['para']['x-token'][i].encode("utf-8").decode("latin1")
                    },
                params={
                    "model_id":self.ModelID
                    }
                )
            try:
                Result=self.Api_SC_Check(Respondata,'GB',i,t)
                self.Result=Result['result']
                print(f"Result:{self.Result}")
            except:
                print(f"Result:{Result}")
    @Rt
    def Api_GET_Balance_IncorrectModelID(self):
        print(f"ApiName: {'GB-ERROR1'}")
        for i in range(6):
            Respondata=requests.get(
                self.para["GB"]['url'],
                headers={
                    "x-token":self.token
                    },
                params={
                    "model_id":self.para["GB"]['para']['x-token'][i].encode("utf-8").decode("latin1")
                    }
                )
            try:
                Result=self.Api_SC_Check(Respondata,'GB',i,t)
                self.Result=Result['result']
                print(self.para["GB"]['para']['x-token'][i])
                print(f"Result:{self.Result}")
            except:
                print(f"ERRORResult:{Result}")
if __name__=="__main__":
    CreateSomething.Mkcsv('apilog',["LogTime","API Name","Status Code","Result"])
    t=1
    while True:
        for i in range(10)[3:7]:
            main=api_test(i)
            main.Api_Get_Token()
            main.Api_GET_Models()
            main.Api_Make_Inference()
            main.Api_Make_Inference_Incorrectmodelid()
            main.Api_Make_Inference_IncorrectBase64()
            main.Api_GET_Inference()
            main.Api_GET_Inference_Incorrectinferid()
            main.Api_GET_PDF_Inference()
            main.Api_GET_PDF_Inference_Incorrectinferid()
            main.Api_GET_Balance()
            main.Api_GET_Balance_IncorrectModelID()
            with open("apilog.csv","a",newline="",encoding="utf8") as file:
                writer=csv.writer(file)
                writer.writerow([f"{t}次測試"])
            print(f"{t}次測試")
            t+=1