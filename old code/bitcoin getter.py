from preparingdata import listgetter
import json
rawdata=open("../data/bitcoininfo.json", "r")
r=rawdata.read()
json=json.loads(r)
print(len(listgetter.listdate(json)))
print(listgetter.listdate(json))

