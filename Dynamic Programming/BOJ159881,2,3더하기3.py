import sys
input = sys.stdin.readline
T = int(input())
case = []
for i in range(T):
    n = int(input())
    case.append(n)

dp = [0,1,2,4]
for i in range(4,max(case)+1):
    dp.append((dp[i-1]+dp[i-2]+dp[i-3])%1000000009)
for i in range(T):
    print(dp[case[i]]%1000000009)