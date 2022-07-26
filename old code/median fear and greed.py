import json
import time
rawdata=open("../data/fearandgreed.json", "r")
r=rawdata.read()
json=json.loads(r)


num=0
def timestamps(json, num):
    return int(((json["data"])[-(num+1)])["timestamp"])

"""
print(timestamps(json, num))
print(len((json["data"])))
"""
def valuefearandgreed(json, num):
    return int(((json["data"])[num])["value"])
"""
def valueaday(x, json):
    firsttimestamp=1517443200
    secondaday=86400

    while day<len((json["data"])):
    x1=firsttimestamp+secondaday*day
    x2=firsttimestamp+secondaday*(day+1)
    num=0
    x=timestamps(json,num)
        while x=>x1 and x<x2:

def listcreation(json):

"""


def median(values):
    lenght=len(values)
    print(lenght)
    tot=0
    x=0
    while x<lenght:
        tot=tot+values[x]
        x=x+1
    return tot/lenght

def valuesday(json, day):
    firsttimestamp=1517443200
    secondaday=86400
    values=[]
    x1=firsttimestamp+secondaday*day
    x2=firsttimestamp+secondaday*(day+1)
    x=0
    while timestamps(json,x)<timestamps(json,(len((json["data"]))-1)):
        if timestamps(json,x)>=x1 and timestamps(json,x)<x2:
            values.append(valuefearandgreed(json,x))
        else:
            break
        x=x+1
    return values

def function(json):
    x=0
    list=[]
    print(len((json["data"])))
    while x<len((json["data"])):
        print("x")
        list.append(median(valuesday(json,x)))
        x=x+1
    return list
print(function(json))