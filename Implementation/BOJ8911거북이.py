T = int(input())
dx = [0,-1,0,1]
dy = [1,0,-1,0]
def robot(move):
    x = 0
    y = 0
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    direc = 0
    for i in move:
        if i == 'F':
            x = x + dx[direc]
            y = y + dy[direc]
        if i == 'B':
            x = x + dx[(direc + 2)%4]
            y = y + dy[(direc + 2)%4]
        if i == 'L':
            if direc == 3:
                direc = 0
            else:
                direc += 1
        if i == 'R':
            if direc == 0:
                direc = 3
            else:
                direc -= 1

        min_x = min(x,min_x)
        min_y = min(y,min_y)
        max_x = max(x,max_x)
        max_y = max(y,max_y)
    ans = (max_x-min_x)*(max_y-min_y)
    print(ans)
for i in range(T):
    move = list(input())
    robot(move)