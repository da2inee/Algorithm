N = int(input())
world = [[0]* 100 for _ in range(100)]

for i in range(N):
    left, bottom = map(int,input().split())
    for j in range(10):
        for k in range(10):
            w = left + j
            h = bottom + k
            world[w][h] += 1
cnt = 0
for i in range(100):
    for j in range(100):
        if world[i][j] >= 1:
            cnt +=1
print(cnt)