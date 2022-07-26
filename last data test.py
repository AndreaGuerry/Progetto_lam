from preparingdata import finaldata
import json

rawdatafagt = open("data/fearandgreed.json", "r")
rfagt = rawdatafagt.read()
jsonfagt = json.loads(rfagt)

rawdatafagtest = open("data/fearandgreedtest.json", "r")
rfagtest = rawdatafagtest.read()
jsonfagtest = json.loads(rfagtest)

rawdatabit = open("data/bitcoininfo.json", "r")
rbit = rawdatabit.read()
jsonbit = json.loads(rbit)

rawdatabitest = open("data/bitcoininfotest.json", "r")
rbitest = rawdatabitest.read()
jsonbitest = json.loads(rbitest)


x_train=finaldata.x_train(jsonfagt,jsonbit)
y_train=finaldata.y_train(jsonbit)

x_test=finaldata.x_test(jsonfagtest,jsonbitest)
y_test=finaldata.y_test(jsonbitest)
print(x_test[0])
print(y_test[0])
print(x_train[0])
print(y_train[0])