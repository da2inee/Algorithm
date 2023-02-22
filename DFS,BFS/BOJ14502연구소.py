from collections import deque
from itertools import combinations
N,M = map(int,input().split())
virus = []
for i in range(N):
    virus.append(list(map(int,input().split())))
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def bfs():
    global ans
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            q = deque()
            if world[i][j] == 2:
                q.append((i,j))
                visited[i][j] = 1
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                            if world[nx][ny] == 0:
                                visited[nx][ny] = 1
                                q.append((nx,ny))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if world[i][j] == 0 and visited[i][j] == 0:
                cnt += 1
    ans = max(ans,cnt)
    return ans
ans = 0
wall = []
world = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if virus[i][j] == 0:
            wall.append([i,j])
for k in combinations(wall,3):
    for i in range(N):
        for j in range(M):
            world[i][j] = virus[i][j]
    
    world[k[0][0]][k[0][1]] = 1
    world[k[1][0]][k[1][1]] = 1
    world[k[2][0]][k[2][1]] = 1
    bfs()
print(ans)

                
#스스로 혼자 풀어서 한번에 맞아서 아주 기분 좋다!! 많이 성장한 것 같다.