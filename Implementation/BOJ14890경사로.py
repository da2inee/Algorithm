N, L = map(int,input().split())
world= []
for i in range(N):
    world.append(list(map(int,input().split())))
def slide(way):
    for j in range(1,N):
        if abs(way[j] - way[j-1]) > 1:
            return False
        if way[j] - way[j-1] == 1:
            for k in range(1,L+1):
                if (j-k) < 0 or way[j-1] != way[j-k] or used[j-k]:
                    return False
                if way[j-1] == way[j-k]:
                    used[j-k] = True
        elif way[j] - way[j-1] == -1:
            for k in range(1,L+1):
                if (j+k) > N or way[j] != way[j+k-1] or used[j+k-1]:
                    return False 
                if way[j] == way[j+k-1]:
                    used[j+k-1] = True
    return True

ans = 0
for i in range(N):
    used = [False] * N 
    if slide([world[i][j] for j in range(N)]):
        ans +=1
for i in range(N):
    used = [False] * N
    if slide([world[j][i] for j in range(N)]):
        ans += 1
print(ans)
                        




