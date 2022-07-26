def date(json, num):
    return (json[-(num + 1)])["Date"]


def dernier(json, num):
    value = (json[-(num + 1)])["Dernier"]
    value=value.replace(".","")
    num1 = value.replace(",", ".")
    value = float(num1)
    return value


def ouv(json, num):
    value = (json[-(num + 1)])["Ouv."]
    value = value.replace(".", "")
    num1 = value.replace(",", ".")
    value = float(num1)
    return value


def plushaut(json, num):
    value = (json[-(num + 1)])["Plus Haut"]
    value = value.replace(".", "")
    num1 = value.replace(",", ".")
    value = float(num1)
    return value


def plusbas(json, num):
    value = (json[-(num + 1)])["Plus Bas"]
    value = value.replace(".", "")
    num1 = value.replace(",", ".")
    value = float(num1)
    return value


def vol(json, num):
    x = (json[-(num + 1)])["Vol."]
    valeur = x[:-1]
    num1 = valeur.replace(",", ".")
    valeur = float(num1)
    multiplicateur = x[-1]
    if multiplicateur == "K":
        nummultiplicateur = 1000
    elif multiplicateur == "M":
        nummultiplicateur = 1000000
    else:
        nummultiplicateur = 1
    value = float(valeur * nummultiplicateur)
    return value
