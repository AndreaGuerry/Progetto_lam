from preparingdata import timestamps
from preparingdata import valuefearandgreed
import json
rawdata=open("../data/fearandgreed.json", "r")
r=rawdata.read()
json=json.loads(r)
x=0
firsttimestamp = 1517443200
secondaday = 86400
values = []
x1 = firsttimestamp + secondaday * 0
x2 = firsttimestamp + secondaday * (0 + 1)
if timestamps.timestamps(json, x) >= x1 and timestamps.timestamps(json, x) < x2:
    values.append(valuefearandgreed.valuefearandgreed(json, x))
else:
    pass
print(values)
print(int(((json["data"])[-(0+1)])["value"]))