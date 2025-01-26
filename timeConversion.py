

def secondsToMinSec(seconds):
    minutes = 0
    while seconds >= 60:
        seconds -= 60
        minutes += 1
    
    return str(minutes) + ":" + str(seconds)

    

def secondsToTime(seconds, time_format="mm:ss"):

    if time_format == "mm:ss":
        return secondsToMinSec(seconds)

