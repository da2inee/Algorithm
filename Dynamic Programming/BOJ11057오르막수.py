from itertools import combinations
N = int(input())
num = []
for comb in combinations(range(0,10),N):
    comb = list(comb)
    num.append(comb)
print(len(num))