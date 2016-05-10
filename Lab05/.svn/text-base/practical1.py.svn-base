import glob
def rowSumIsValid(mat):
    sum = 0
    asum = 0
    for i in mat[0]:
        sum += i
    for c in mat:
        for j in c:
            asum += j
        if asum != sum:
            return False
        asum = 0
    return True

def columnSumIsValid(mat):
    sum = 0
    asum = 0
    length = 0
    for i in mat:
        sum += i[0]
        length = len(i)
    #print(sum)
    #print(length)
    for j in range(0,length):
        for i in mat:
            asum += i[j]
            #print(asum)
        if asum != sum:
            return False
        else:
            asum = 0
    return True


def magicSquareIsValid(filepath):
    matrix = []
    with open(filepath,'r') as file:
        lines = file.readlines()
        for i in range(0,len(lines)):
            s = lines[i].split()
            l = []
            for item in s:
                l.append(int(item))
            matrix.append(l)
    if (columnSumIsValid(matrix) and rowSumIsValid(matrix)):
        return True
    else:
        return False
def getTotalCost(itemSet):
    output = {}
    files = [f for f in glob.glob("Stores/*")]
    for filename in files:
        name = filename.split('/')[1].split('.')[0]
        cost = float(0)
        with open(filename,'r') as file:
            lines = file.readlines()
            for i in range(3,len(lines)):
                s = lines[i].split()
                for item in itemSet:
                    if (item[0] == s[0]+" "+s[1]):
                        cost += item[1]*float(s[3].replace("$",""))
                        #print("Cost:".format(cost))
                        #print("UnitP:".format(float(s[3].replace("$",""))))
        output.update({name:round(cost,2)})
    return output
def getBestPrices(cpuSet):
    output = {}
    files = [f for f in glob.glob("Stores/*")]
    for item in cpuSet:
        min = 99999999
        l = []
        for filename in files:
            name = filename.split('/')[1].split('.')[0]
            with open(filename,'r') as file:
                lines = file.readlines()
                for i in range(3,len(lines)):
                    s = lines[i].split()
                    if (item == s[0]+" "+s[1]):
                        if(float(s[3].replace("$","")) < min):
                                min = float(s[3].replace("$",""))
                                l.append(name)
        output.update({item:(min,l[len(l)-1])})
    return output

def getMissingItems():
    output = {}
    files = [f for f in glob.glob("Stores/*")]
    for filename in files:
        name = filename.split('/')[1].split('.')[0]
        CPUS = []
        nCPUS = set()
        with open(filename,'r') as file:
            lines = file.readlines()
            for i in range(3,len(lines)):
                s = lines[i].split()
                CPUS.append(s[0]+" "+s[1])
                #print(CPUS)
            for fn in files:
                if(fn != filename):
                    with open(fn,'r') as fl:
                        ls = fl.readlines()
                        for j in range(3,len(ls)):
                            g = ls[j].split()
                            cpu = g[0]+" "+g[1]
                            #print(cpu)
                            if cpu not in CPUS:
                                nCPUS.add(g[0]+" "+g[1])
        output.update({name:nCPUS})
    return output


if __name__ == '__main__':
    pass