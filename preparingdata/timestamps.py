def timestamps(json, num):
    #print(((json["data"])[-(num+1)])["timestamp"])
    return int(((json["data"])[-(num+1)])["timestamp"])