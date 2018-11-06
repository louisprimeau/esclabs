def ge_fw(A):

    B = list(A)

    if(len(B) <= 1):
        return(B)

    greatestentry = 0
    for i in range(0,len(B),1): # Step 1
        if(B[i][0] > greatestentry):
            hold = list(B[i])
            B[i] = list(B[0])
            B[0] = list(hold)
            break

    if(B[0][0] == 0): #If Zero Matrix, return
        return(B)

    for i in range(1,len(B),1): #Step 2
        for j in range(1,len(B[i]),1):
            B[i][j] = B[i][j] - (B[i][0] / B[0][0]) * B[0][j]
        B[i][0] = 0

    C = ge_fw([i[1:] for i in B[1:]]) #Step 3
    for i in range(0,len(C),1):
        B[i+1][1:] = C[i]

    return(B)

def ge_bw(A):
    B = list(A)

    if(len(B) <= 1):
        return(B)

    lastnonzero = 0
    for i in range(len(B)-1,-1,-1):
        if(B[i][0] != 0):
            for j in range(1,len(B[i]),1):
                B[i][j] = B[i][j] / B[i][0]
            B[i][0] = 1
            lastnonzero = i
            break
    print(B)
    for i in range(0,lastnonzero,1):
        for j in range(1,len(B[i]),1):
            B[i][j] = B[i][j] - (B[i][0] / B[lastnonzero][0]) * B[lastnonzero][j]
        B[i][0] = 0
    print(B)

    C = ge_bw(i[1:] for i in B[0:lastnonzero] + B[lastnonzero+1:len(B)])
    print(C)
    for i in range(0,lastnonzero,1):
        B[i][1:] = C[i]
    for i in range(lastnonzero+1,len(C),1):
        B[i][1:] = C[i]

    return(B)
