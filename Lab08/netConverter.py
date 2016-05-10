from HardwareTasks import *

def verilog2vhdl(line):
    try:
        t = processLine(line)
        s = t[1] + ': ' + t[0] + ' PORT MAP('
        for item in t[2]:
            s += item[0]+ '=>' + item[1] + ', '
        s = s[0:-2] + ');'
        return s
    except:
        return 'Error: Bad Line.'

def convertNetlist(source, actual):
    with open(source,'r') as file:
        lines = file.readlines()
    inf = []
    for line in lines:
        inf.append(verilog2vhdl(line))
    with open(actual,'w') as wfile:
        wfile.write('\n'.join(inf))

if __name__ == '__main__':
    pass