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

    B = list(A) #Assign return matrix

    index = [0,0]
    for i in range(len(A)-1,-1,-1):
        for j in range(0,len(A[i]),1):
            if(A[i][j] != 0):
                index = [i,j]

    if(len(B) <= 1): #If too small do nothing
        return(B)
    if(B[0][0] == 0):
        return(B)
    for i in range(0,len(B[ index[0] ]),1): #Normalize last nonzero row
        B[ index[0] ][i] = B[ index[0] ][i] / B[ index[0] ][ index[1] ]

    for i in range(0,index[0],1): #Zero out nonzero row lead zero column
        for j in range(0,len(B[i]),1):
            B[i][j] -= (B[i][ index[1] ] / B[ index[0] ][ index[1] ]) * B[ index[0] ][j]

    C = ge_bw((i[ 0:index[1] ] + i[ index[1]+1:len(B[0]) ]) for i in B[ 0:index[0] ] + B[ index[0]+1:len(B) ]) #Generate the submatrix, perform backwards again and assign to C

    #Illegal but conceptually easier
    B[0:index[0]][0:index[1]] = C[0:index[0]][0:index[1]]
    B[index[0]:len(B)][0:index[1]] = C[index[0]-1:len(C)][0:index[1]]
    B[0:index[0]][index[1]:len(B)] = C[0:index[0]][index[1]-1:len(C)]
    B[index[0]:len(B)][index[1]:len(B)] = C[index[0]-1:len(C)][index[1]-1:len(C)]


    return(B)
