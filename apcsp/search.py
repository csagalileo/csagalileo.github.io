import time

def search1(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
        print("Searching...")
    return found

def search2(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
        print("Searching...")
    return found

size = int(input("List size? (choose a number between 1 to 1000000, 0 to exit) "))
while (size > 0):
    startTime = time.time()
    search1(range(size), -1)
    print ('search1 took', (time.time() - startTime)*1000, 'milliseconds.')
    startTime = time.time()
    search2(range(size), -1)
    print ('search2 took', (time.time() - startTime)*1000, 'milliseconds.')
    size = int(input("List size? (choose a number between 1 to 1000000, 0 to exit) "))
    
