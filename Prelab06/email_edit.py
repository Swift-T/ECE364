import re

def main():
    with open('Part2.in','r') as fin:
        lines = fin.readlines()
    for line in lines:
        line = line.strip('\n')
        line = re.sub(r'(purdue.edu)',r'ecn.\1',line)
        line = re.sub(r'(\d$)',r'\1/100',line)
        print(line)

if __name__ == '__main__':
    main()