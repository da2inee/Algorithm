from itertools import permutations
N = int(input())
array = list(permutations([1,2,3,4,5,6,7,8,9],3))
for i in range(N):
    a,b,c = map(int,input().split())
    a = list(str(a))
    remove_cnt = 0
    for k in range(len(array)):
        strike = 0
        ball = 0
        k -= remove_cnt
        for i in range(3):
            a[i] = int(a[i])
            if a[i] == array[i]:
                strike += 1
            elif int(a[i]) != array[i] and array[i] in a:
                ball += 1
        if ball == c and strike == b:
            continue
        else:
            array.remove(array[k])
            remove_cnt += 1
print(len(array))

