from logging import exception
import pandas,csv
import requests,time,re
from bs4 import BeautifulSoup
'''
368
efai123
lose 206
'''
pattern = re.compile(r'BONE AGE: [0-9]*.[0-9]*')
with open('log_standard.csv','w',encoding='utf-8-sig',newline="") as file:
    write = csv.writer(file)
    write.writerow(['PatientID','Gender','Age','Bone Age'])

for i in range(368):
    if i < 10 :
        url = f'http://192.168.5.202/ai/1317050017/BADICOM-00{i}.dcm/BADICOM-00{i}.dcm'
    elif i>=10 and i<100:
        url = f'http://192.168.5.202/ai/1317050017/BADICOM-0{i}.dcm/BADICOM-0{i}.dcm'
    else:
        url = f'http://192.168.5.202/ai/1317050017/BADICOM-{i}.dcm/BADICOM-{i}.dcm'

    print(url)

    try:
        data = requests.get(url).text
        BS = BeautifulSoup(data,'html.parser')    
    except:
        print('the data wrong')

    try:
        ALL_Patient = BS.find('div','card my-1')
        print(ALL_Patient.find_all('li')[0].text)
        print(ALL_Patient.find_all('li')[2].text)
        print(ALL_Patient.find_all('li')[3].text)
    except:
        with open('losenum.txt','a+',encoding='utf-8') as file:
            file.write(str(i)+'\n')
        print(f'{i} no content so continue')
        print('\n'*2)
        continue
    try:
        patientid = re.split(r':',ALL_Patient.find_all('li')[0].text)[-1].strip()
        patientgender = re.split(r':',ALL_Patient.find_all('li')[2].text)[-1].strip()
        patientage = re.split(r':',ALL_Patient.find_all('li')[3].text)[-1].strip()
    except:
        raise exception('split error')
    try:
        ALL_Report = BS.find(id='prediction')
        match = re.match(pattern,ALL_Report.text)
        match = re.split(r':',match.group())[-1]

        with open('log_standard.csv','a',encoding='utf-8-sig',newline="") as file:
            write = csv.writer(file)
            write.writerow([patientid,patientgender,patientage,match])
    except:
        with open('losenum.txt','a+',encoding='utf-8') as file:
            file.write(str(i)+'\n')

    print('\n'*2)
    # time.sleep(5)
