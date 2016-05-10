import re
import sys
import os.path

def main():
    if len(sys.argv) == 2:
        if not os.path.exists(sys.argv[1]):
            print("Error: Could not read "+sys.argv[1])
        with open(sys.argv[1]) as fin:
            lines = fin.readlines()
        for line in lines:
            matches = re.match(r'def (.*)\((.*)\)',line)
            if matches:
                print(matches.groups()[0])
                arg = matches.groups()[1].split(",")
                for i,a in enumerate(arg):
                    print("Arg" + str(i+1)+": "+a.replace(" ",""))
    else:
        print("Usage: function_finder.py [python_file_name]")
if __name__ == "__main__":
    main()