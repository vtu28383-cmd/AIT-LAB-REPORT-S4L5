list=[[],[2,3,4,6],[1,6,5,4],[1,4,5],[6,3],[3],[4,2,1]]
vis=[]
dfs=[]
for i in range(len(list)+1):
    vis.append(-1)
stack=[]
stack.append(1)
vis[1]=1
while len(stack)!=0:
    temp=stack.pop()
    dfs.append(temp)
    for i in list[temp]:
        if(vis[i]!=1):
            stack.append(i)
            vis[i]=1
            break
print(dfs)
    
