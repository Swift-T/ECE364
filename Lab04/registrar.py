import glob

def getDetails():
    output = {}
    student = {}
    with open("files/students.txt",'r') as file:
        lines = file.readlines()
        for i in range(2,len(lines)):
            s = lines[i].split()
            student.update({s[4]:s[0]+" "+s[1]+" "+s[2]})
    files = [f for f in glob.glob("files/EECS*")]
    for filename in files:
        course = filename.split('/')[1].split('.')[0].replace("EECS","")
        with open(filename,'r') as file:
            lines = file.readlines()
            for i in range(2,len(lines)):
                s = lines[i].split()
                t = (course,round(float(s[1])))
                if student[s[0]] in output.keys():
                    output[student[s[0]]].add(t)
                else:
                    output.update({student[s[0]]:{t}})
    return output

def getStudentList(className):
    output = []
    student = {}
    with open("files/students.txt",'r') as file:
        lines = file.readlines()
        for i in range(2,len(lines)):
            s = lines[i].split()
            student.update({s[4]:s[0]+" "+s[1]+" "+s[2]})
    files = [f for f in glob.glob("files/EECS*")]
    for filename in files:
        course = filename.split('/')[1].split('.')[0].replace("EECS","")
        if className == course:
            with open(filename,'r') as file:
                lines = file.readlines()
                for i in range(2,len(lines)):
                    s = lines[i].split()
                    output.append(student[s[0]])
    output.sort()
    return output

def searchForName(Name):
    output = {}
    student = {}
    with open("files/students.txt",'r') as file:
        lines = file.readlines()
        for i in range(2,len(lines)):
            s = lines[i].split()
            student.update({s[4]:s[0]+" "+s[1]+" "+s[2]})
    files = [f for f in glob.glob("files/EECS*")]
    for filename in files:
        course = filename.split('/')[1].split('.')[0].replace("EECS","")
        with open(filename,'r') as file:
            lines = file.readlines()
            for i in range(2,len(lines)):
                s = lines[i].split()
                if student[s[0]] == Name:
                    output.update({course:round(float(s[1]))})
    return output

def searchForID(ID):
    output = {}
    student = {}
    with open("files/students.txt",'r') as file:
        lines = file.readlines()
        for i in range(2,len(lines)):
            s = lines[i].split()
            student.update({s[4]:s[0]+" "+s[1]+" "+s[2]})
    files = [f for f in glob.glob("files/EECS*")]
    for filename in files:
        course = filename.split('/')[1].split('.')[0].replace("EECS","")
        with open(filename,'r') as file:
            lines = file.readlines()
            for i in range(2,len(lines)):
                s = lines[i].split()
                if ID in student.keys():
                    if ID == s[0]:
                        output.update({course:round(float(s[1]))})
    return output

def findScore(studentname,classnum):
    student = {}
    with open("files/students.txt",'r') as file:
        lines = file.readlines()
        for i in range(2,len(lines)):
            s = lines[i].split()
            student.update({s[4]:s[0]+" "+s[1]+" "+s[2]})
    files = [f for f in glob.glob("files/EECS*")]
    for filename in files:
        course = filename.split('/')[1].split('.')[0].replace("EECS","")
        if(classnum == course):
            with open(filename,'r') as file:
                lines = file.readlines()
                for i in range(2,len(lines)):
                    s = lines[i].split()
                    if student[s[0]] == studentname:
                        return int(s[1])
    return None

def getHighest(classnum):
    output = ()
    student = {}
    max = -1
    with open("files/students.txt",'r') as file:
        lines = file.readlines()
        for i in range(2,len(lines)):
            s = lines[i].split()
            student.update({s[4]:s[0]+" "+s[1]+" "+s[2]})
    files = [f for f in glob.glob("files/EECS*")]
    for filename in files:
        course = filename.split('/')[1].split('.')[0].replace("EECS","")
        if(classnum == course):
            with open(filename,'r') as file:
                lines = file.readlines()
                for i in range(2,len(lines)):
                    s = lines[i].split()
                    if max < round(float(s[1])):
                        max = round(float(s[1]))
                        output = (student[s[0]],max)

    return output

def getLowest(classnum):
    output = ()
    student = {}
    max = 999
    with open("files/students.txt",'r') as file:
        lines = file.readlines()
        for i in range(2,len(lines)):
            s = lines[i].split()
            student.update({s[4]:s[0]+" "+s[1]+" "+s[2]})
    files = [f for f in glob.glob("files/EECS*")]
    for filename in files:
        course = filename.split('/')[1].split('.')[0].replace("EECS","")
        if(classnum == course):
            with open(filename,'r') as file:
                lines = file.readlines()
                for i in range(2,len(lines)):
                    s = lines[i].split()
                    if max > round(float(s[1])):
                        max = round(float(s[1]))
                        output = (student[s[0]],max)
    return output

def getAverageScore(studentName):
    student = {}
    total = float(0)
    count = 0
    with open("files/students.txt",'r') as file:
        lines = file.readlines()
        for i in range(2,len(lines)):
            s = lines[i].split()
            student.update({s[4]:s[0]+" "+s[1]+" "+s[2]})
    if(studentName not in student.values()):
        return None
    files = [f for f in glob.glob("files/EECS*")]
    for filename in files:
        course = filename.split('/')[1].split('.')[0].replace("EECS","")
        with open(filename,'r') as file:
            lines = file.readlines()
            for i in range(2,len(lines)):
                s = lines[i].split()
                if student[s[0]] == studentName:
                    total += float(s[1])
                    count += 1
    return round(total/count,1)

if __name__ == '__main__':
    pass