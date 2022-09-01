import requests
import zipfile


def loader():
    daypermonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = 3
    day = 1
    year = 2021
    done = False

    while year <= 2022 and done == False:
        while month < 12 and done == False:
            day = 1

            if len(str(month)) == 1:
                monthdigit = ("0{}".format((month + 1)))
            else:
                monthdigit = (month + 1)


            date = ("BTCUSDC-5m-{}-{}-{}.zip".format(year, monthdigit, daydigit))

            print(date)
            if year == 2022 and monthdigit == "07" :
                done = True
                break
            else:
                pass
            day = day + 1

        month = month + 1
    month = 1
    year = year + 1


print(loader())

url = "https://data.binance.vision/data/spot/monthly/klines/BTCUSDC/5m/BTCUSDC-5m-2021-12.zip"
resp = requests.get(url)
open("binance data.zip", "wb").write(resp.content)
with zipfile.ZipFile("binance data.zip", 'r') as zip_ref:
    zip_ref.extractall("binancedata")
