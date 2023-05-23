n=int(input())
l=list(map(int,input().split()))
s1=0
s2=0
for i in range(n):
    if i%2==0 or i==0:
        s1=s1+l[i]
        #even
    else:
        s2=s2+l[i]
        #odd
a=s2-s1
if a==0:
    print("YES")
else:
    print("NO")