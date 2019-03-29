def sortr(L):
    i = 0
    hold = []
    while(1):
        buckets = [[]] * 10
        for l in L:
            buckets[digit(l,i)] = buckets[digit(l,i)] + [l]
        i += 1
        if(L == merge(buckets)):
            break
        L = merge(buckets)
    return(L)
def digit(x,i):
    return(int(str(x // 10**i)[len(str(x // 10**i)) - 1]))
def merge(L):
    a = []
    for l in L:
        a = a + l
    return(a)
print(sortr([13231412,23112114,33213213,42512152,53434,623125]))
