import requests
import zipfile
import os
import pandas as pd


def dategetter(num):
    firstmonth = 4
    month = firstmonth + num
    if month <= 12:
        year = 2021
    else:
        year = 2022
        month = month - 12
    if len(str(month)) == 1:
        monthdigit = ("0{}".format((month)))
    else:
        monthdigit = (month)
    date = ("{}-{}".format(year, monthdigit))
    return date


def urlgetter(date):
    url = ("https://data.binance.vision/data/spot/monthly/klines/BTCUSDC/5m/BTCUSDC-5m-{}.zip".format(date))
    return url


def csvgetter(url, date):
    resp = requests.get(url)
    open("Csvdata.zip", "wb").write(resp.content)
    with zipfile.ZipFile("Csvdata.zip", 'r') as zip_ref:
        zip_ref.extractall("binancedata")
    os.remove("Csvdata.zip")
    f=open("binancedata/BTCUSDC-5m-{}.csv".format(date))
    tot=open("binancedata/tot.csv", "a")
    tot.write(f.read())
    f.close()
    os.remove("binancedata/BTCUSDC-5m-{}.csv".format(date))


def final():
    f=open("binancedata/tot.csv","w")
    f.write("open time, open, high, low, close, volume, close time, quote asset volume, number of trade, taker base asset volume, taker buy quote asset volume, ignore")
    f.close()
    for a in range(16):
        date=dategetter(a)
        print(date)
        url=urlgetter(date)
        csv=csvgetter(url, date)


def convert():
    df = pd.read_csv(r'binancedata/tot.csv')
    df.to_json(r'binancedata/tot.json')


#open time, open, high, low, close, volume, close time, quote asset volume, number of trade, taker base asset volume, taker buy quote asset volume, ignore

#csvgetter(urlgetter(dategetter(0)))
convert()

