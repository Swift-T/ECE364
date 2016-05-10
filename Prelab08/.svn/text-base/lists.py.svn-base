import statistics

def find_median(l1,l2):
    ml = l1+l2
    if len(ml) % 2 == 0:
        return (int(statistics.median(ml[0:-1])),sorted(ml))
    else:
        return (int(statistics.median(ml)),sorted(ml))

if __name__ == "__main__":
    l1 = list(map(int,input("Enter the first list of numbers: ").split()))
    l2 = list(map(int,input("Enter the second list of numbers: ").split()))
    m,ml = find_median(l1,l2)
    print('First list:',l1)
    print('Second list:',l2)
    print('Merged list:',ml)
    print('Median:',m)