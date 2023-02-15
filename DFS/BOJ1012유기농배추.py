from collections import deque
T = int(input())
def warm(M,N,K):
    world = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    for _ in range(K):
        X,Y = map(int,input().split())
        world[Y][X] = 1
    q = deque()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    ans = 0
    for i in range(N):
        for j in range(M):
            if world[i][j] == 1 and visited[i][j] == 0:
                q.append((i,j))
                visited[i][j] = 1
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < M:
                            if visited[nx][ny] == 0 and world[nx][ny] == 1:
                                visited[nx][ny] = 1
                                q.append((nx,ny))
                ans += 1
    print(ans)
for _ in range(T):
    M, N, K = map(int,input().split())
    warm(M,N,K)