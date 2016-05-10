def addNumbers(num):
    r=0
    for i in range(0,num+1):
       r += i
    return r

def addMultiplesOf(num):
    m = range(0,1001,num)
    return sum(m)

def getNumberFrequency(num):
    var = "The value of Pi is 3 . 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5 0 2 8 8 4 1 9 7 1 6 9 3 9 9 3 7 5 1 0 5 8 2 0 9 7 4 9 4 4 5 9 2 3 0 7 8 1 6 4 0 6 2 8 6 2 0 8 9 9 8 6 2 8 0 3 4 8 2 5 3 4 2 1 1 7 0 6 7 9 8 2 1 4 8 0 8 6 5 1 3 2 8 2 3 0 6 6 4 7 0 9 3 8 4 4 6 0 9 5 5 0 5 8 2 2 3 1 7 2 5 3 5 9 4 0 8 1 2 8 4 8 1"
    return var.count(str(num))

def getDigitalSum(nstr):
    total = 0
    for i in range(0,len(nstr)):
        total += (ord(nstr[i])-48)
    return total

def getSequenceWithoutDigit(digit):
    strList = ["736925233695599303035509581762617623184956190649483967300203776387436934399982","943020914707361894793269276244518656023955905370512897816345542332011497599489","627842432748378803270141867695262118097500640514975588965029300486760520801049","153788541390942453169171998762894127722112946456829486028149318156024967788794","981377721622935943781100444806079767242927624951078415344642915084276452000204","276947069804177583220909702029165734725158290463091035903784297757265172087724","474095226716630600546971638794317119687348468873818665675127929857501636341131"]
    full = "".join(strList)
    prev = ""
    output = ""
    max = 0
    num = str(digit)
    for c in full:
        if num != c:
            output += c

        else:
            if max < len(output):
                max = len(output)
                prev = output
            output = ""
    return prev

def capitalizeMe(stript):
    stript = stript.title()
    output = ""
    for i in stript.split():
        output += i[:-1]+i[-1].upper()+" "
    return output[:-1]
if __name__ == '__main__':
    pass