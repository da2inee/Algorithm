N = int(input())
N = str(N)
cnt = 0
for i in range(1,len(N)):
    cnt += i*(10**(i-1)*9)

cnt += ((int(N)-(10**(int(len(N))-1)) + 1) * int(len(N)))
print(cnt)
