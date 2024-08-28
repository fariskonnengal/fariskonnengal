x = int(input("enter the first number"))
y = int(input("enter the second number"))
z = int(input("enter the third number"))

if x<y<z or x<z<y:
    print(x,"is the smallest")
elif y<x<z or y<z<x:
    print(y,"is the smallest")
else:
    print(z,"is the smallest")