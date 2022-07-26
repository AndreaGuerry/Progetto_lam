import json
from preparingdata import function
from preparingdata import timestamps
rawdata=open("../data/fearandgreed.json", "r")
r=rawdata.read()
json=json.loads(r)

lol=function.function(json)
lol[72]=23
lol[73]=24
lol[74]=25
