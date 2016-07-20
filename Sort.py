def insertionSort(myList):
    for i in range(1,len(myList)):
        currentValue = myList[i]
        position = i

        while position>0 and myList[position-1]>currentValue:
            myList[position] = myList[position-1]
            position = position-1

        myList[position]=currentValue
        
myList=[67, 45, 2, 13, 1, 998]
print('Check out my supremely unsorted list')
print(myList)
insertionSort(myList)
print('Check out my dazzlingly sorted list')
print(myList)
