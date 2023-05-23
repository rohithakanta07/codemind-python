n=int(input())
l=list(map(int,input().split()))
s=0
s2=0
for i in range(n):
    if i%2==0 or i==0:
        s=s+l[i]
    else:
        s2=s2+l[i]
if (abs(s2-s))%4==0:
    print("X")
else:
    print("Y")