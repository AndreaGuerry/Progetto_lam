from preparingdata import datagetter

def listdate(json):
    dates=[]
    x=0
    while x<len(json):
        dates.append(datagetter.date(json, x))
        x=x+1
    return dates

def listdernier(json):
    derniers=[]
    x=0
    while x<len(json):
        derniers.append(datagetter.dernier(json, x))
        x=x+1
    return derniers

def listouv(json):
    ouvs=[]
    x=0
    while x<len(json):
        ouvs.append(datagetter.ouv(json, x))
        x=x+1
    return ouvs

def listplushaut(json):
    plushauts=[]
    x=0
    while x<len(json):
        plushauts.append(datagetter.plushaut(json, x))
        x=x+1
    return plushauts

def listplusbas(json):
    pointsbas=[]
    x=0
    while x<len(json):
        pointsbas.append(datagetter.plusbas(json, x))
        x=x+1
    return pointsbas

def listvol(json):
    vols=[]
    x=0
    while x<len(json):
        vols.append(datagetter.vol(json, x))
        x=x+1
    return vols