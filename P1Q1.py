a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

if a%2==0 and b%2==0 and c%2==0:
    print("Please enter odd numbers!")
if a%2!=0 or b%2!=0 or c%2!=0:
    if a>b and a>c :
        print("a is the largest number")
    elif b>a and b>c :
        print("b is the largest number")
    else :
        print("c is the largest number")
elif a%2!=0 and b%2!=0 :
    if a>b :
        print("a is the largest number")
    else:
        print("b is the largest number ")
elif b%2!=0 and c%2!=0 :
    if b>c :
        print("b is the largest number")
    else:
        print("c is the largest number ")
elif c%2!=0 and a%2!=0 :
    if c>a :
        print("c is the largest number")
    else:
        print("a is the largest number ")
