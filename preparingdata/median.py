def median(values):
    lenght=len(values)
    tot=0
    x=0
    if lenght==0:
        return ("none")
    else:
        while x<lenght:
            tot=tot+values[x]
            x=x+1
        return tot/lenght