from preparingdata import listgetter
from preparingdata import resizer
from preparingdata import function
from preparingdata import serialconverter


def x_train(json, json1):
    fandg = function.function(json)
    fandg[72] = 23
    fandg[73] = 24
    fandg[74] = 25
    dernier = listgetter.listdernier(json1)
    ouv = listgetter.listouv(json1)
    plusbas = listgetter.listplusbas(json1)
    plushauts = listgetter.listplushaut(json1)
    vol = listgetter.listvol(json1)
    x=resizer.dataformater(fandg, dernier, ouv, plusbas, plushauts, vol)
#    return serialconverter.serialencoderm3(x)
    return x

def y_train(json):
    plusbas = listgetter.listplusbas(json)
    plushauts = listgetter.listplushaut(json)
    x=resizer.resultformater(plusbas, plushauts)
    #    return serialconverter.serialencoder(x)
    return x

def x_test(json,json1):
    fandg = function.functiontest(json)
    dernier = listgetter.listdernier(json1)
    ouv = listgetter.listouv(json1)
    plusbas = listgetter.listplusbas(json1)
    plushauts = listgetter.listplushaut(json1)
    vol = listgetter.listvol(json1)
    x=resizer.dataformater(fandg, dernier, ouv, plusbas, plushauts, vol)
    #    return serialconverter.serialencoderm3(x)
    return x

def y_test(json):
    plusbas = listgetter.listplusbas(json)
    plushauts = listgetter.listplushaut(json)
    x=resizer.resultformater(plusbas, plushauts)
    #   return serialconverter.serialencoder(x)
    return x