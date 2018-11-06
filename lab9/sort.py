def bubbleSort(a):
    swapped = True
    if(type(a) != list):
        return(False)
    while(swapped):
        swapped = False
        for i in range(1,len(a)):
            if(a[i-1] > a[i]):
                hold = a[i]
                a[i] = a[i-1]
                a[i-1] = hold
                swapped = True
    return(True)
