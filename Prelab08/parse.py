import sys,os
if __name__ == "__main__":
    try:
        with open(sys.argv[1],'r') as file:
            lines = file.readlines()
        for line in lines:
            l = line.split()
            total = 0
            count = 0
            note = ''
            for num in l:
                try:
                    total += int(num)
                    count += 1
                except ValueError:
                    note += num + ' '
            if total:
                print(format(round(float(total)/float(count),3),'.3f') + ' ' + note)
            else:
                print(note)
    except IndexError:
        print('Usage: parse.py [filename]')
    except IOError:
        print(sys.argv[1] + 'is not a readable file.')