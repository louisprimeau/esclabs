from stackLib import stack

def bc(expression):
    paren = ['{','[','(','}',']',')']
    output = [True,-1]
    st = stack()
    for i in range(0,len(expression),1):
        if(expression[i] in paren[0:3]):
            st.push(expression[i])
        elif((expression[i] in paren[3:len(paren)]) and ((len(st.a) == 0) or ((paren.index(expression[i]) + 3) == paren.index(st.pop())))):
                output[0] = False
                output[1] = i
                break
    if(len(st.a) != 0 and output[0] == True):
        output[0] = False
    print(st.a)
    return(output)
