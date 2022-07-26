from preparingdata import listgetter
import json
from preparingdata import function
from preparingdata import resizer
from preparingdata import serialconverter
from preparingdata import converter


rawdata = open("../data/bitcoininfo.json", "r")
r = rawdata.read()
json2 = json.loads(r)

rawdata1 = open("../data/fearandgreed.json", "r")
r1 = rawdata1.read()
json1 = json.loads(r1)

fandg = function.function(json1)
fandg[72] = 23
fandg[73] = 24
fandg[74] = 25
print(fandg)

date = listgetter.listdate(json2)
dernier = listgetter.listdernier(json2)
ouv = listgetter.listouv(json2)
plusbas = listgetter.listplusbas(json2)
plushauts = listgetter.listplushaut(json2)
vol = listgetter.listvol(json2)

trainingdata = resizer.dataformater(fandg, dernier, ouv, plusbas, plushauts, vol)

print(len(trainingdata))


print(resizer.resultformater(plusbas, plushauts))

unnom=serialconverter.serialencoder(trainingdata)

print(len(unnom[0]))
print(len(unnom[-1]))

deuxnom=serialconverter.serialdecoder(unnom)
print(deuxnom[0])

x1=converter.encoder(100)
x2=converter.decoder(x1)
print(x1)
print(x2)