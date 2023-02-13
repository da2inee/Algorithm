word = list(input())
ans = []
for i in range(1,len(word)-1):
    for j in range(i+1,len(word)):
        x = word[:i]
        x.reverse()
        y = word[i:j]
        y.reverse()
        z = word[j:]
        z.reverse()
        ans.append(x+y+z)
ans.sort()
print(''.join(ans[0]))