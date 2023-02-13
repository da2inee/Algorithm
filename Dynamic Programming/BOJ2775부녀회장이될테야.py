T = int(input())
def people(k,n):
    house = [[i for i in range(1,n+1)] for _ in range(k+1)]
    for w in range(1,k+1):
        for h in range(1,n):
            house[w][h] = house[w-1][h] + house[w][h-1]
            print(house)
    print(house[k][n-1])
for i in range(T):
    k = int(input())
    n = int(input())
    people(k,n)