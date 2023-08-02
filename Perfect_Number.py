def per_num(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    if s==n:
        return True
    return False
n=int(input())
res=per_num(n)
print(res)