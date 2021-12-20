import requests, json, pymysql, sys,time
def Get_Resource_Tojson(arg):
    def decorator(func):
        def wrapper(*args,**kwargs):
            Dat= requests.get(arg)
            Dat=Dat.text
            print(type(Dat))
            Datj= json.load(Dat)
            print(type(Datj))
            kwargs= Dat
            # return func(kwargs)
            return 'OK'
        return wrapper
    return decorator

@Get_Resource_Tojson('https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json')
def Parser_Datj(kwargs=None):
    return kwargs

if __name__== '__main__':
    print(Parser_Datj())