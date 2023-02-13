from collections import deque
N,K = map(int,input().split())
q = deque()
for i in range(1,N+1):
    q.append(i)
ans = []
while q:
    for i in range(K-1):
        x = q.popleft()
        q.append(x)
    
    ans.append(q.popleft())
print("<",end="")
for i in range(len(ans)-1):
    print("%d, "%ans[i],end='')
print(ans[-1],end='')
print('>')
    

    
