matrix=[[0,1,1],
       [0,0,0],
       [0,0,0]]
def traversal(matrix,i,j,list):
    if(i==len(matrix)-1 and j==len(matrix[0])-1):
        list.append((i,j))
        print(list)
        list.pop()
        return
    list.append((i,j))
    if(i+1<len(matrix)):
        if(matrix[i+1][j]!=1):
           traversal(matrix,i+1,j,list)
    if(j+1<len(matrix[0])):
        if(matrix[i][j+1]!=1):
            traversal(matrix,i,j+1,list)
    list.pop()
traversal(matrix,0,0,[])
       
