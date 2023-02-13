N = int(input())
home = []
for i in range(N):
    home.append(list(map(int,input().split())))
dp = [0,0,0]
dp[0] = home[0][0]
dp[1] = home[0][1]
dp[2] = home[0][2] 
a = 0
for i in range(1,N):
    if a == 0:
        dp[] 