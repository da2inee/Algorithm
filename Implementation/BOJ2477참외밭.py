K = int(input())
width = 0
height = 0
width_idx = 0
height_idx = 0
world = []
for i in range(6):
    x,y = map(int,input().split())
    world.append([x,y])
    if x == 1 or x == 2:
        width = max(width,y)
    if x == 3 or x == 4:
        height = max(height,y)
for i in range(6):
    if world[i][1] == width:
        width_idx = i
    if world[i][1] == height:
        height_idx = i
cnt = height*width

if width_idx == 0:
    w =  abs(world[-1][1]-world[1][1])
elif width_idx == 5:
    w =  abs(world[4][1]-world[0][1])
elif 0<width_idx<5:
    w = abs(world[width_idx-1][1]-world[width_idx+1][1])
if height_idx == 0:
    h = abs(world[-1][1]-world[1][1])
elif height_idx == 5:
    h = abs(world[4][1]-world[0][1])
elif 0<height_idx<5:
    h = abs(world[height_idx-1][1]-world[height_idx+1][1])
cnt -= w*h
print(cnt*K)

