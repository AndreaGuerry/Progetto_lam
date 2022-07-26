from preparingdata import median
from preparingdata import valuesday


def function(json):
    x = 0
    list = []
    while x <= ((len(json["data"])) + 2):
        list.append(median.median(valuesday.valuesday(json, x)))
        x = x + 1
    return list


def functiontest(json):
    x = 0
    list = []
    while x <= ((len(json["data"]))-1):
        list.append(median.median(valuesday.valuesdaytest(json, x)))
        x = x + 1
    return list
