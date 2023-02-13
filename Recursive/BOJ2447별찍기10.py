N = int(input())
world = [[' 'for _ in range(N)] for _ in range(N)]

def star(size,x,y):
    if size == 1:
        world[x][y] = "*"
    else:
        new_size = size //3
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    star(new_size,x+i*new_size,y +j*new_size)
star(N,0,0)
for i in world:
    print(''.join(i))