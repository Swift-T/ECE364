import re

def idIsAcceptable(string):
    if re.search(r'^[A-Za-z1-9]+$|^[_A-Za-z1-9]+$|^[_A-Za-z1-9_]+$',string) is None:
        return False
    else:
        return True

def processSingle(string):
    match = re.match(r'^\.([A-Za-z0-9]+)\(([A-Za-z_]+[0-9]+|[A-Za-z]|_[1-9]+_|[a-z_]+|[0-1])\)$',string)
    if match is None:
        raise ValueError()
    else:
        return match.groups()[0],match.groups()[1]

def processLine(line):
    matchl1 = re.match(r'^\s*([A-Za-z0-9]+)\s+([A-Za-z0-9_]+)\s+\((.+)\)$',line)
    assignment = []
    if matchl1 is None:
        raise ValueError()
    else:
        ports = matchl1.groups()[2].replace(' ','').split(',')
        for port in ports:
            try:
                assignment.append(processSingle(port))
            except:
                raise ValueError()
        return matchl1.groups()[0],matchl1.groups()[1],tuple(assignment)

if __name__ == '__main__':
    processLine('First U22 (.A(n32),.B(n5),.C(n3),.D(n6),.Y(n25)))')