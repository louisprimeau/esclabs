def quicksort(L,ini,fin):
    if(fin-ini == 0):
        return(True)
    if(fin - ini == 1):
        return(True)
    if(fin - ini == 2):
        if(L[ini] > L[fin-1]):
            L[ini],L[fin-1] = L[fin-1],L[ini]
            return(True)
        else:
            return(True)
    pivot = partition(L,ini,fin)
    quicksort(L,ini,pivot)
    quicksort(L,pivot+1,fin)
    return(True)
def partition(L,ini,fin):
    pivot = ini
    for i in range(ini,ini + fin-ini,1):
        print(L)
        if(L[i] < L[pivot]):
            L[ini:fin] = L[ini:pivot] + [L[i]] + L[pivot:i] + L[i+1:fin]
            pivot += 1

    return(pivot)
def hanoi(n,start,tmp,final):
   if n > 0:
        hanoi(n - 1,start,final,tmp)
        final.append(start.pop())
        hanoi(n - 1,tmp,start,final)
        print(start,tmp,final)
        return True
   else:
        return True


hanoi(7,[0,1,2,3,4,5,6],[],[])
