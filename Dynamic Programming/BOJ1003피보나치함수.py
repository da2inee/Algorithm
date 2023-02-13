T = int(input())
def fibo(n):
    ans = [0,0]
    zero = [1,0,1]
    one = [0,1,1]
    if n <= 2:
        ans[0] = zero[n]
        ans[1] = one[n]
        print(*ans)
        return
    else:
        for i in range(3,n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
            
        ans[0] = zero[n]
        ans[1] = one[n]
        print(*ans)
for i in range(T):
    fibo(int(input()))
    
        

        
