import json
from preparingdata import datagetter
rawdata=open("../data/bitcoininfo.json", "r")
r=rawdata.read()
json=json.loads(r)

dates=[]
derniers=[]
ouvs=[]
plushauts=[]
plusbas=[]
vols=[]

print(len(json))
x=0
while x<len(json):
    dates.append(datagetter.date(json, x))
    x=x+1
print(dates)