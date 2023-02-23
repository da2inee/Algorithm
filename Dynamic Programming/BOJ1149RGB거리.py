N = int(input())
world = []
for i in range(N):
    world.append(list(map(int,input().split())))
dp = [[0]*3 for _ in range(N)]
dp[0][0] = world[0][0]
dp[0][1] = world[0][1]
dp[0][2] = world[0][2]
for i in range(1,N):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + world[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + world[i][1]
    dp[i][2] = min(dp[i-1][1],dp[i-1][0]) + world[i][2]
print(min(dp[-1]))