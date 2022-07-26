from preparingdata import datagetter
from preparingdata import function
from preparingdata import listgetter
import json
from preparingdata import resizer
from preparingdata import serialconverter

rawdata = open("../data/fearandgreedtest.json", "r")
r = rawdata.read()
json2 = json.loads(r)

rawdata1 = open("../data/fearandgreed.json", "r")
r1 = rawdata1.read()
json1 = json.loads(r1)

rawdata2 = open("../data/bitcoininfo.json", "r")
r2 = rawdata2.read()
json3 = json.loads(r2)

fandg = function.function(json1)
fandg[72] = 23
fandg[73] = 24
fandg[74] = 25

date = listgetter.listdate(json3)
dernier = listgetter.listdernier(json3)
ouv = listgetter.listouv(json3)
plusbas = listgetter.listplusbas(json3)
plushauts = listgetter.listplushaut(json3)
vol = listgetter.listvol(json3)
trainingdatatest = resizer.dataformater(fandg, dernier, ouv, plusbas, plushauts, vol)
tra=serialconverter.serialencoderm3(trainingdatatest)
print(tra[0])
