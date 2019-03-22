def selection_sort(u):
    for i in range(0,len(u)-1,1):
        minindex = i + u[i:len(u)].index(min(u[i:len(u)]))
        u[i],u[minindex] = u[minindex],u[i]
    return True
def heapify(u):
    for i in range(1,len(u),1):
        added = i
        while(1):
            if(u[added] < u[added//2]): u[added], u[added//2] = u[added//2], u[added]
            else: break
            added = added // 2
    return True
def reheapify(u,end):

    if(len(u) - end == 2):
        if(u[end] > u[end + 1]):
            u[end + 1],u[end] = u[end],u[end + 1]
            print(u, end = ' ')
            return(True)
        else:
            print(u, end = ' ')
            return(True)

    u[end:len(u)] = u[len(u)-1:] + u[end:len(u)-1]
    print(u,end=' ')
    print("moved")
    index = 1
    while(1):
        if(index * 2 + end - 1 < len(u) and index * 2 + end < len(u) and (u[end + index - 1] > u[index * 2 + end - 1] or u[end + index - 1] > u[index * 2 + end])):
            if(u[index * 2 + end] > u[index * 2 + end - 1]):
                u[end + index - 1], u[index * 2 + end - 1] = u[index * 2 + end - 1], u[end + index - 1]
                index = index * 2
            else:
                u[end + index - 1], u[index * 2 + end] = u[index * 2 + end], u[end + index - 1]
                index = index * 2 + 1
        else:
            break
    print(u,end = ' ')
    return True
def heap_sort(u):
    heapify(u)
    print(u, end = ' ')
    print("heaped")
    for i in range(1,len(u),1):
        print(u[i:len(u)])
        reheapify(u,i)
        print("reheaped")
    return(True)
def helper_merge_sort(u,start,end):
    if((end-start) == 1):
        return(True)
    elif((end-start) <= 2):
        if(u[start] < u[start + 1]):
            return(True)
        else:
            u[start],u[start + 1] = u[start + 1],u[start]
            return(True)
    helper_merge_sort(u,start,start + (end - start)//2)
    helper_merge_sort(u,start + (end - start)//2,end)
    helper_merge(u,start,end,start + (end - start)//2)
    return(True)
def merge_sort(u,start,end):
    helper_merge_sort(u,0,len(u))
    return(True)
def helper_merge(u,start,end,middle):
    uindex = start
    vindex = middle
    while(1):
        if(uindex == vindex): break
        if(vindex >= end): break
        if(u[uindex] <= u[vindex]):
            uindex += 1
        elif(u[uindex] > u[vindex]):
            u[:] = u[0:uindex] + [u[vindex]] + u[(uindex):vindex] + u[(vindex + 1):len(u)]
            uindex += 1
            vindex += 1
    return(True)
