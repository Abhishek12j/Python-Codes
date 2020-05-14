#Exercise 2- Faulty calculator
print("Enter 1st number:",end=" ")
a=int(input())
print("Enter 2nd number:",end=" ")
b=int(input())
print("Enter operator:",end=" ")
o=input()
if a==45 and b==3 and o=="*" :
    print(555)
elif a==56 and b==9 and o=="+" :
    print(77)
elif a==56 and b==4 and o=="/" :
    print(4)
else :
    if o=="+" :
        print(a+b)
    elif o=="-" :
        print(a-b)
    elif o=="*" :
        print(a*b)
    elif o=="/" :
        print(a/b)
    elif o=="^" :
        print(a**b)
    else :
        print("Invalid operator")
