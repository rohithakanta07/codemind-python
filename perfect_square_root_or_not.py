import math 
def perf_sq(n):
    for i in range (1,n//2+1):
        if n == i*i :
            return True 
    return False
n=int(input())
res=perf_sq(n)
if res==True :
    print("True")
else:
    print("False")