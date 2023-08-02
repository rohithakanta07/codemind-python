def pronic_num(n):
    for i in range(1,num):
        if i*(i+1)==num:
            return True
    return False
            
num=int(input())
res=pronic_num(num)
if res==True:
    print("YES")
else:
    print("NO")
