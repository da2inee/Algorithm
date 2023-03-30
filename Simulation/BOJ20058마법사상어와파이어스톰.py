from collections import deque
N,Q = map(int,input().split())
world = []
for _ in range(2**N):
    world.append(list(map(int,input().split())))
L = list(map(int,input().split()))

def bfs(world,x):
    dx = [0,-1,1,0]
    dy = [1,0,0,-1]
    visited = [[0]*(2**N) for _ in range(2**N)]
    n = int(2**(N-x))
    for xx in range(n):
        for yy in range(n):
            for k in range(4):
                nx = xx*(2**x) 
                ny = yy *(2**x)
                if 0<=nx<2**N and 0<=ny<2**N:
                    for i in range(2**x):
                        for j in range(2**x):
                            visited[nx +j][ny + 2**x-1-i] = world[nx +i][ny +j]
    for i in range(2**N):
        for j in range(2**N):
            world[i][j] = visited[i][j]
    for i in range(2**N):
        for j in range(2**N):
            cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx<2**N and 0<=ny<2**N:
                    if visited[nx][ny] >0:
                        cnt += 1
            if cnt <3:
                world[i][j] -= 1                    
    return world

for i in range(Q):
    bfs(world,L[i])

ans = 0
q = deque()
for i in range(2**N):
    for j in range(2**N):
        if world[i][j] >=0:
            ans += world[i][j]
visited = [[0]*(2**N) for _ in range(2**N)]
dx = [0,-1,1,0]
dy = [1,0,0,-1]
ans2 = 0
for i in range(2**N):
    for j in range(2**N):
        a = 0
        if world[i][j] > 0 and visited[i][j] == 0:
            q.append((i,j))
            visited[i][j] = 1
            a += 1
            while q:
                x,y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<2**N and 0<=ny<2**N:
                        if visited[nx][ny] == 0 and world[nx][ny] >0:
                            q.append((nx,ny))
                            visited[nx][ny] = 1
                            a += 1
        ans2 = max(ans2,a)

print(ans)
print(ans2)