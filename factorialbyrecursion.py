def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1

        while(n > 1):
            fact *= n
            n -= 1
        return fact
n=int(input("enter the number"))
print(n,"factorial is",factorial(n))