
class Simulation:

    def __init__(self,*args):
        self.simulationNumber = int(args[0])
        self.simulationDate = args[1]
        self.chipName = args[2]
        self.chipCount = int(args[3])
        self.chipCost = round(float(args[4]),2)
        self.simulationCost = round(self.chipCount * self.chipCost,2)

    def __str__(self):
        s = self.chipName + ': ' + format(self.simulationNumber,'03d') + ', '+ self.simulationDate + ', $'+ format(self.simulationCost,'06.2f')
        return s

class Employee:

    def __init__(self,*args):
        self.employeeName = args[0]
        self.employeeID = args[1]
        self.simulationsDict = {}

    def __str__(self):
        s = self.employeeID + ', ' + self.employeeName + ': '+ format(len(self.simulationsDict),'02d') + ' Simulations'
        return s

    def addSimulation(self, sim):
        if sim.simulationNumber not in self.simulationsDict.keys():
            self.simulationsDict.update({sim.simulationNumber:sim})
        else:
            self.simulationsDict[sim.simulationNumber] = sim

    def getSimulation(self, num):
        if num in self.simulationsDict.keys():
            return self.simulationsDict[num]
        else:
            return None

    def getWorkload(self):
        s = str(self) + '\n'
        c= {}
        for key,value in self.simulationsDict.items():
            c.update({value.chipName:key})
        l = list(c.keys())
        l.sort()
        a = ''
        for name in l:
            a += str(self.simulationsDict[c[name]]) + '\n'
        s += a
        return s.rstrip('\n')

    def addWorkload(self,filename):
        with open(filename,'r') as file:
            lines = file.readlines()
        for i in range(2,len(lines)):
            s = lines[i].split()
            if len(s) == 5:
                self.addSimulation(Simulation(s[0],s[1],s[2],s[3],s[4].strip('$')))

class Facility:

    def __init__(self,*args):
        self.facilityName = args[0]
        self.employeesDict = {}

    def __str__(self):
        s = self.facilityName + ': ' + format(len(self.employeesDict.keys()),'02d') + ' Employees\n'
        c= {}
        for key,value in self.employeesDict.items():
            c.update({value.employeeID:key})
        l = list(c.keys())
        l.sort()
        a = ''
        for ID in l:
            a += str(self.employeesDict[c[ID]]) + '\n'
        s += a
        return s.rstrip('\n')

    def addEmployee(self, e):
        if e.employeeName not in self.employeesDict.keys():
            self.employeesDict.update({e.employeeName:e})
        else:
            self.employeesDict[e.employeeName] = e

    def getEmployees(self,*args):
        l = []
        for name in args:
            if name in self.employeesDict.keys():
                l.append(self.employeesDict[name])
        return l

    def getSimulation(self,num):
        for key,value in self.employeesDict.items():
            if value.getSimulation(num) is not None:
                return value.getSimulation(num)
        return None

if __name__ == '__main__':
    pass

