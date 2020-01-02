def LCS(X, Y, i): 
    C = [[0] * (i+1) for x in range(i+1)]

    # Create the bottom up table C
    for row in range(i+1): 
        for col in range(i+1): 
            if row == 0 or col == 0: 
                C[row][col] = 0
            elif X[row-1] == Y[col-1]: 
                C[row][col] = C[row-1][col-1] + 1
            else: 
                C[row][col] = max(C[row-1][col], C[row][col-1])

    # Starting from the bottom right corner of the table, traverse backwards to find the subsequence.
    index = C[i][i]
    ret = ""
    row = i
    col = i
    # While we have not reached the top left corner yet:
    while row != 0 and col != 0:
        # Char is in the subsequence, concat to the substring you will return at the end.
        # Next cell to traverse to will be one row up and one column left
        if X[row-1] == Y[col-1]: 
            ret = X[row-1] + ret 
            row = row - 1
            col = col - 1
            index = index - 1
        # Cell above current one is greater than cell one left to the current one, move one row up.
        elif C[row-1][col] >= C[row][col-1]: 
            row = row - 1
        # Cell one left to the current one is greater than cell above current one, move one column left.
        else: 
            col = col - 1
    print(C)
    return ret
        

def read_and_call_LCS(input):
    seq_file = open(input,"r")
    seq_info = seq_file.readlines()
    seq_n = int(seq_info[0])
    str1 = seq_info[1]
    str2 = seq_info[2]
    
    output_string = LCS(str1,str2,seq_n)
    output = open("output","a")
    output.write(output_string)
    seq_file.close()
    output.close()

read_and_call_LCS("03_input")