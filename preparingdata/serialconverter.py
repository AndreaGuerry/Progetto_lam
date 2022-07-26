from preparingdata import converter


def serialencoder(list):
    x = 0
    while x < len(list):
        x1 = 0

        while x1 < len(list[x]):
            (list[x])[x1] = converter.encoder((list[x])[x1])
            x1 = x1 + 1
        x = x + 1
    return list


def serialencoderm3(list):
    x = 0
    while x < len(list):
        x1 = 0
        while x1 < len(list[x1]):
            x2 = 0
            lol=(list[x])[x1]
            while x2 < len(lol):
                ((list[x])[x1])[x2] = converter.encoder(((list[x])[x1])[x2])
                x2 = x2 + 1
            x1 = x1 + 1
        x = x + 1
    return list


def serialdecoder(list):
    x = 0
    while x < len(list):
        x1 = 0

        while x1 < len(list[x]):
            (list[x])[x1] = converter.decoder((list[x])[x1])
            x1 = x1 + 1
        x = x + 1
    return list
