N,M = map(int,input().split())
world = [[0] * (M+1)]

for i in range(N):
    world.append(list(map(int,input().split())))
for i in range(1,N+1):
    world[i].insert(0,0)

dp = [[0] * M for _ in range(N)]
dp[0][0] == world[0][0]
for i in range(1,N+1):
    for j in range(1,M+1):
        world[i][j] = max(world[i-1][j],world[i][j-1],world[i-1][j-1]) + world[i][j]
print(world[N][M])
