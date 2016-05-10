try:
    from timeDuration import *
except ImportError:
    print("Unable to import 'timeDuration'.")
def getTotalEventSpan(ex):
    with open('Events.txt','r') as file:
        lines = file.readlines()
    days = 0
    weeks = 0
    hours = 0
    for line in lines:
        if line[4:11] == ex:
            if line[20] == 'h':
                hours += int(line[18:20]) * int(line[31])
            if line[20] == 'd':
                days += int(line[18:20]) * int(line[31])
            if line[20] == 'w':
                weeks += int(line[18:20]) * int(line[31])
    return TimeSpan(weeks,days,hours)
def rankEventsBySpan(*args):
    time = []
    for ex in args:
        total = getTotalEventSpan(ex).getTotalHours()
        time.append((ex,total))
    time = sorted(time,key=lambda t:t[1],reverse=True)
    result = []
    for i in time:
        result.append(i[0])
    return result