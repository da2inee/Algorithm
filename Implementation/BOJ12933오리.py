duck = list(input())
quack = list('quack')
visited = [0]* len(duck)
ans = 0
def cry(start):
    global cnt
    j = 0
    first = 1
    for i in range(start,len(duck)):
        if duck[i] == quack[j] and visited[i] == 0:
            visited[i] = 1
            j += 1
            if duck[i] == 'k':
                if first:
                    cnt += 1
                    j = 0
                    first = 0
                else:
                    j = 0


        

if len(duck) % 5 != 0:
    print(-1)
    exit()

cnt  = 0
for i in range(len(duck)):
    if duck[i] == 'q' and visited[i] == 0:
        cry(i)
if cnt == 0 or not all(visited): 
    print(-1)

else: 
    print(cnt)
