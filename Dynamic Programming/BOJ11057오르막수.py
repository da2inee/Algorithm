#dp 문제는 항상 규칙을 찾으려고 노력하자!!
N = int(input())
dp = [[1]*10 for _ in range(N)]

for i in range(1,N):
    for j in range(1,10):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
ans = 0
for i in range(10):
    ans += dp[N-1][i]

print(ans%10007)