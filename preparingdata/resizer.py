def listresizer(list):
    dataset = []
    x = 0
    while x <= (len(list) - 200):
        interval = list[x:(x + 200)]
        dataset.append(interval)
        x = x + 1
    return dataset


def dataformater(fandg, dernier, ouv, plusbas, plushauts, vol):
    dataset = []
    oneblocdata = []
    x = 0
    while x <= ((len(fandg)) - 201):
        intervalfandq = fandg[x:(x + 200)]
        intervaldernier = dernier[x:(x + 200)]
        intervalouv = ouv[x:(x + 200)]
        intervalplusbas = plusbas[x:(x + 200)]
        intervalplushauts = plushauts[x:(x + 200)]
        intervalvol = vol[x:(x + 200)]
        oneblocdata = intervalfandq + intervaldernier + intervalouv + intervalplusbas + intervalplushauts + intervalvol
        dataset.append(oneblocdata)
        x = x + 1
    return dataset


def resultformater(plusbas, plushauts):
    dataset = []
    oneblocdata = []
    x = 0
    while x <= ((len(plusbas)) - 201):
        intervalplusbas = plusbas[(x + 200)]
        intervalplushauts = plushauts[(x + 200)]
        oneblocdata = [intervalplusbas, intervalplushauts]
        dataset.append(oneblocdata)
        x = x + 1
    return dataset

def dataformater(fandg, dernier, ouv, plusbas, plushauts, vol):
    dataset = []
    oneblocdata = []
    x = 0
    while x <= ((len(fandg)) - 201):
        intervalfandq = fandg[x:(x + 200)]
        intervaldernier = dernier[x:(x + 200)]
        intervalouv = ouv[x:(x + 200)]
        intervalplusbas = plusbas[x:(x + 200)]
        intervalplushauts = plushauts[x:(x + 200)]
        intervalvol = vol[x:(x + 200)]
        oneblocdata.append(intervalfandq)
        oneblocdata.append(intervaldernier)
        oneblocdata.append(intervalouv)
        oneblocdata.append(intervalplusbas)
        oneblocdata.append(intervalplushauts)
        oneblocdata.append(intervalvol)
        dataset.append(oneblocdata)
        x = x + 1
        oneblocdata=[]
    return dataset
