N = int(input())
key = list(map(int,input().split()))
ans = [0]*N
for i in range(N):
    num = key[i]
    cnt = 0 
    for j in range(N):
        if ans[j] == 0:
            cnt += 1
        if cnt == num+1:
            ans[j] = i+1
            break
print(*ans)