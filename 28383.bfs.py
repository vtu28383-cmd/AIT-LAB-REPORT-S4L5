list=[
    [1,3],
    [0,2],
    [1,4],
    [0,2],
    [2]
    ]
queue=[]
vis=[0,0,0,0,0]
queue.append(0)
vis[0]=1
arr=[]
arr.append(0)
while len(queue)!=0:
    temp=list[queue[0]]
    for i in temp:
        if vis[i]==0:
            arr.append(i)
            queue.append(i)
            vis[i]=1
    queue.pop(0)
print(arr)
    
