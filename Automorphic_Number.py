n=int(input())
no_of_digits=len(str(n))
sq=n*n
last_digit=sq%pow(10,no_of_digits)
if (last_digit==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")