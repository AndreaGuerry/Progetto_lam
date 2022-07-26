import math

def encoder(value):
    pi=math.pi
    x=(math.atan(value))/(1/2*pi)
    return x

def decoder(value):
    pi=math.pi
    y=(math.tan(value*(1/2)*pi))
    return y