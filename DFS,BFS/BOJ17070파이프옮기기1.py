N = int(input())
world = []
for i in range(N):
    world.append(list(map(int,input().split())))
cnt = 0
def dfs(now):
    global cnt
    x,y,z = now
    if x == N-1 and y == N-1:
        cnt += 1
        return 
    if z == 0 or z == 1:
        if 0<=y+1<N and world[x][y+1] == 0:
            dfs((x,y+1,0))
    if z == 1 or z == 2:
        if 0<=x+1<N and world[x+1][y] == 0:
            dfs((x+1,y,2))
    if z == 0 or z == 1 or z == 2:
        if 0<=x+1<N and 0<=y+1<N and world[x][y+1] == 0 and world[x+1][y] == 0 and world[x+1][y+1] == 0:
            dfs((x+1,y+1,1))
dfs((0,1,0))
print(cnt)



    

#bfs로 풀면 시간초과난다. 범위가 크면 dfs로 풀기. 이것도 부족하다면 dp도 생각해보기