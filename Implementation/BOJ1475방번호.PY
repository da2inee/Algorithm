N = list(input())
num = [0]*9

for i in range(len(N)):
    N[i] = int(N[i])
    if N[i] == 9 or N[i] == 6:
        num[6] += 1
    else:
        num[N[i]] += 1
if num[6] % 2 == 0:
    num[6] = num[6]//2
elif num[6] % 2 == 1:
    num[6] = (num[6] //2) +1
print(max(num))

    
