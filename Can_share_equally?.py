x,y=map(int,input().split())
a=(x*1)+(y*2)
#if a%2==0:
if x==0 and y%2==0:
    print("YES")
elif x!=0 and x%2==0:
    print("YES")
else:
    print("NO")