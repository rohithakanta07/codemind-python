n=int(input())
s=0
temp=n
while(n>0):
    r=n%10
    s=s+r
    n=n//10
p=1
while(temp>0):
    r=temp%10
    p=p*r
    temp=temp//10
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")
