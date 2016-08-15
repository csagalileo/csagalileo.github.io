import time
import random

def sort1(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def sort2(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        sort2(lefthalf)
        sort2(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

def sort3(alist, size):
    buckets = []
    for j in range(size):
        buckets.append(0)
    for i in range(size):
        buckets[alist[i]] += 1
    i = 0
    for j in range(size):
        for k in range(buckets[j]):
            alist[i] = j
            i += 1
    

size = int(input("List size? (choose a number between 10 to 1000, 0 to exit) "))
while (size > 0):
    listOfNumbers = []
    for x in range(size):
        listOfNumbers.append(random.randint(0, size-1))
    startTime = time.time()
    sort1(listOfNumbers)
    print ('sort1 took', (time.time() - startTime)*1000, 'milliseconds.')
    listOfNumbers = []
    for x in range(size):
        listOfNumbers.append(random.randint(0, size-1))
    startTime = time.time()
    sort2(listOfNumbers)
    print ('sort2 took', (time.time() - startTime)*1000, 'milliseconds.')
    listOfNumbers = []
    for x in range(size):
        listOfNumbers.append(random.randint(0, size-1))
    startTime = time.time()
    sort3(listOfNumbers, size)
    print ('sort3 took', (time.time() - startTime)*1000, 'milliseconds.')
    size = int(input("List size? (choose a number between 10 to 1000, 0 to exit) "))
    
