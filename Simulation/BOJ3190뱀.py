from collections import deque
N = int(input())
K = int(input())
apple = [[0]*N for _ in range(N)]
for i in range(K):
    x,y = map(int,input().split())
    apple[x-1][y-1] = 2
L = int(input())
direction = dict()
dx = [0,1,0,-1]
dy = [1,0,-1,0]
now = 0
for i in range(L):
    X, C = input().split()
    direction[int(X)] = C
q = deque()
q.append((0,0))
def left(C):
    global now
    if C == 'L':
        now = (now -1) % 4
    else:
        now = (now + 1) % 4
cnt = 0
x= 0
y = 0
apple[x][y] = 1
while 1:
    cnt += 1
    x += dx[now]
    y += dy[now]
    if x < 0 or y<0 or x>=N or y>=N:
        break
    if apple[x][y] == 2:
        apple[x][y] = 1
        q.append((x,y))
        if cnt in direction:
            left(direction[cnt])
    elif apple[x][y] == 0:
        apple[x][y] = 1
        q.append((x,y))
        a,b = q.popleft()
        apple[a][b] = 0
        if cnt in direction:
            left(direction[cnt])
    else:
        break
print(cnt)

