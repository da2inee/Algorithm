N,M = map(int,input().split())
world = []
for i in range(N):
    world.append(input())
x = 0
y = 0
ans = 0
for k in range(1,min(N,M)):
    size = k
    for i in range(N):
        for j in range(M):
            if (i + size) < N and (j + size) < M:
                if world[i][j] == world[i][j+size]==world[i+size][j]==world[i+size][j+size]:
                    ans = max(ans,size)
print((ans+1)**2)
