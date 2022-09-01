import json


# open time, open, high, low, close, volume, close time, quote asset volume, number of trade, taker base asset volume, taker buy quote asset volume, ignore


def openget(json, num):
    value = (json[" open"])[str(num)]
    return value


def highget(json, num):
    value = (json[" high"])[str(num)]
    return value


def lowget(json, num):
    value = (json[" low"])[str(num)]
    return value


def closeget(json, num):
    value = (json[" close"])[str(num)]
    return value


def volget(json, num):
    value = (json[" volume"])[str(num)]
    return value


def numbtradeget(json, num):
    value = (json[" number of trade"])[str(num)]
    return value


def datapatch(json, num):
    high = highget(json, num)
    low = lowget(json, num)
    openv = openget(json, num)
    close = closeget(json, num)
    x = [openv, close, high, low]
    return x


def constructor(json):
    x = []
    y=[]
    a = 0
    b=0
    for b in range(140091-200):
        a = 0
        for a in range(200):
            x.append(datapatch(json, (b+a)))
        y.append(x)
        x=[]
    print(len(y))
    return y
