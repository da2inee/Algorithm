N = int(input())
room = []
for i in range(N):
    room.append(list(input()))

weight = 0
height = 0
for i in range(N):
    cnt = 0 
    for j in range(N):
        if room[i][j] == '.':
            cnt +=1
        else:
            cnt = 0 
        if cnt == 2:
            weight +=1
    
for i in range(N):
    cnt = 0 
    for j in range(N):
        if room[j][i] ==  '.':
            cnt +=1
        else:
            cnt = 0
        if cnt == 2:
            height +=1
    
ans = [weight,height]
print(*ans)

#가로,세로 따로 세는것까진 잘 생각했는데, 중간에 X가있을 경우 고려하는것이 어려웠음
#cnt가 2가 되었을때 하나씩 추가해주는 방법을 생각하지 못했음
