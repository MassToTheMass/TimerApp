import datetime

def getSystemTime():
    current_time = datetime.datetime.now().time()

    return current_time

def getSecondsFromHMS(time_string):

    time_list = time_string.split(":")
    seconds = 0
    print(time_list)
    for index, i in enumerate(time_list):
        i = int(i)
        if index == 0:
            seconds += 3600 * i
        elif index == 1:
            seconds += 60 * i
        else:
            seconds += i
    return seconds

def getSecondsFromTime(time_string):

    default = True

    if len(time_string.split(":")) == 3 and default:
        return getSecondsFromHMS(time_string)