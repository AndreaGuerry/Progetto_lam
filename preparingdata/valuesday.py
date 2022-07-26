from preparingdata import timestamps
from preparingdata import valuefearandgreed
def valuesday(json, day):
    firsttimestamp=1517443200
    secondaday=86400
    values=[]
    x1=firsttimestamp+secondaday*day
    x2=firsttimestamp+secondaday*(day+1)
    x=0
    sagrossemèrelagrossetchoinputainjpp=0
    while sagrossemèrelagrossetchoinputainjpp<x2:
        if timestamps.timestamps(json,x)>=x1 and timestamps.timestamps(json,x)<x2:
            values.append(valuefearandgreed.valuefearandgreed(json,x))
        else:
            pass
        x=x+1
        try:
            sagrossemèrelagrossetchoinputainjpp=timestamps.timestamps(json,x)
        except:
            break
    return values

def valuesdaytest(json, day):
    firsttimestamp=1640217600
    secondaday=86400
    values=[]
    x1=firsttimestamp+secondaday*day
    x2=firsttimestamp+secondaday*(day+1)
    x=0
    sagrossemèrelagrossetchoinputainjpp=0
    while sagrossemèrelagrossetchoinputainjpp<x2:
        if timestamps.timestamps(json,x)>=x1 and timestamps.timestamps(json,x)<x2:
            values.append(valuefearandgreed.valuefearandgreed(json,x))
        else:
            pass
        x=x+1
        try:
            sagrossemèrelagrossetchoinputainjpp=timestamps.timestamps(json,x)
        except:
            break
    return values