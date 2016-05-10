import re
import sys

with open(sys.argv[1]) as fin:
    lines = fin.readlines()

for line in lines:
    matches = re.match(r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}:(.*)',line)
    if matches:
        #print(matches.groups())
        if matches.groups()[3].isdigit():
            if int(matches.groups()[3]) < 1024:
                print(matches.group() + ' - Valid (root privileges required)')
            elif int(matches.groups()[3]) < 32767:
                print(matches.group() + ' - Valid')
            else:
                print(matches.group() + ' - Invalid port number')
        else:
            print(matches.group() + ' - Invalid port number')
    else:
        print(line + '- Invalid IP Address')