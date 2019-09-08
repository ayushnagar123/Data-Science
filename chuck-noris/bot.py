from urllib.request import urlopen
import requests
import json
import pandas as pd

url = "http://api.icndb.com/jokes"

url_result = urlopen(url)
data = url_result.read()

json_data = json.loads(data)

res=json_data['value']

head=""
j=res[0]
for i,header in enumerate(j.keys()):
    if(i<len(j)-2):
        head+=header+','
    else:
        if(',' in header):
            header='\"'+header+'"'
        head+=header
        break

with open('jokes.csv','w') as file:
    file.write(head+'\n')
    for i in list(res):
        data=""
        for k,val in enumerate(i.values()):
            if(k<len(i)-2):
                data+=str(val)+','
            else:
                if(',' in val):
                    val = '\"'+val+'"'
                data+=str(val)
                break
        file.write(data+'\n')

l=len(res)

url_input = input()

df = pd.read_csv('jokes.csv')

for i in range(l):
    url_check=url+'/'+str(df.iloc[i][0])
    if(url_input==url_check):
        print(df.iloc[i][1])
        break