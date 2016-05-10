def getPairwiseDifference(slist):
    output = []
    if type(slist) == list and slist:
        for i in range(0,len(slist)-1):
            output.append(slist[i+1]-slist[i])
    else:
        return None
    return output
def flatten(input):
    output = []
    if type(input) != list or not input:
        return None
    for item in input:
        if type(item) != list:
            return None
        else:
            output = output +  item
    return output

def partition(input,num):
    output = []
    i = 0
    if type(input) != list or not input:
        return None
    part = round(len(input)/float(num))
    while i < len(input):
        if i + num >= len(input):
            tmp = input[i:-1]
            tmp += [input[-1]]
            output.append(tmp)
        else:
            output.append(input[i:i+num])
        i += num
    return output

def rectifySignal(input):
    output = []
    if type(input) != list or not input:
        return None
    for item in input:
        if(item < 0):
            output.append(0)
        else:
            output.append(item)
    return output
def floatRange(start, end, step):
    output = []
    if (start >= end):
        return None
    i = start
    while(i <= end):
        output.append(round(i,1))
        i += step
        i = round(i,1)
    return output

def getLongestWord(input):
    if type(input) != str:
        return None
    if len(input.split()) <= 1:
        return None
    return max(input.split(),key=len)

def decodeNumbers(input):
    if type(input) != list:
        return None
    if not all(isinstance(item,int) for item in input):
        return None
    output = ""
    for item in input:
        output += chr(item)
    return output

def getCreditCard(input):
    if type(input) != str or not input:
        return None
    return [ord(item)- 48 for item in input if item.isdigit()]
if __name__ == '__main__':
    pass