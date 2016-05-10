import glob
import filecmp
import string
def getWordFrequency():
    output = {}
    files = [f for f in glob.glob("files/*")]

    for filename in files:
        with open(filename,'r') as file:
            for line in file:
                for s in line.split():
                    s = s.rstrip(",.")
                    if s not in output.keys():
                        output[s] = 1
                    else:
                        output[s] += 1
    return output

def getDuplicates():
    output = {}
    files = [f for f in glob.glob("files/*")]
    grouplist = []
    for filename in files:
        flag = 0
        for group in grouplist:
            if( filecmp.cmp("files/"+group[0]+".txt",filename)):
                flag = 1
                group.append(filename.split('/')[1].split('.')[0])
                group.sort()
                break

        if (flag == 0):
            grouplist.append([filename.split('/')[1].split('.')[0]])
    for group in grouplist:
        count = 0
        with open("files/"+group[0]+".txt",'r') as file:
            count = len(set("".join(l for l in file.read() if l not in string.punctuation).split()))
        #output.update({group[0]:(count,group)})
        if(group[0] not in output.keys()):
            output.update({group[0]:(count,group)})
        else:
            output[group[0]] = (count,group)
    return output

def getPurchaseReport():
    output = {}
    item = {}
    with open("purchases/Item List.txt",'r') as file:
        lines = file.readlines()
        for i in range(2,len(lines)):
            s = lines[i].split()
            item.update({s[0]:s[1].replace('$','')})
    files = [f for f in glob.glob("purchases/purchase*")]
    for filename in files:
        id = int(filename.split('_')[1].split('.')[0])
        total = float(0)
        with open(filename,'r') as file:
            lines = file.readlines()
            for i in range(2,len(lines)):
                s = lines[i].split()
                total += float(item[s[0]]) * float(s[1])
        output.update({id:round(total,2)})
    return output

def getTotalSold():
    output = {}
    with open("purchases/Item List.txt",'r') as file:
        lines = file.readlines()
        for i in range(2,len(lines)):
            s = lines[i].split()
            output.update({s[0]:0})
    files = [f for f in glob.glob("purchases/purchase*")]
    for filename in files:
        with open(filename,'r') as file:
            lines = file.readlines()
            for i in range(2,len(lines)):
                s = lines[i].split()
                output[s[0]] += int(s[1])
    return output
if __name__ == '__main__':
    pass