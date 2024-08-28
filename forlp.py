n= int(input("enter the integer "))
for x in range(n):
    print(x)

for x in range(n):
    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")
#factorial
if n==0 or n==1:
    print("fact is 1")
else:
    fact=1
    i=1
    while(i<=n):
        fact=fact*i
        i+=1
print("factorial is",fact)


