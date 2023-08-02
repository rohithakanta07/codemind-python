n=int(input())
temp=n
sq=n*n
s=0
while(sq>0):
    r= sq%10
    s=s+r
    sq=sq//10
if temp==s:
    print("Neon Number")
else:
    print("Not Neon Number")
