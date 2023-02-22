from collections import deque
while 1:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        exit()
    dx = [0,0,-1,1,1,1,-1,-1]
    dy = [1,-1,0,0,1,-1,1,-1]
    world = []
    for i in range(h):
        world.append(list(map(int,input().split())))
    visited = [[0] * w for _ in range(h)]
    ans = 0
    q = deque()
    for i in range(h):
        for j in range(w):
            if world[i][j] == 1 and visited[i][j] == 0:
                x, y = i, j
                q.append((x,y))
                visited[x][y] = 1
                ans += 1
                while q:
                    x,y = q.popleft()
                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        
                        if 0 <= nx < h and 0 <= ny < w:                       
                            if world[nx][ny] == 1 and visited[nx][ny] == 0:
                                visited[nx][ny] = 1
                                q.append((nx,ny))
    print(ans)

