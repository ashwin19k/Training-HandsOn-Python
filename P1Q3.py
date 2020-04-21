a=[]
for x in range (1,11):
    b=int(input("Enter the number"+str(x)+":"))
    a.append(b)

c=[]
d=[]
for i in a:
    if i%2==0:
        c.append(i)
    else :
        d.append(i)

d.sort()


if len(d) == 0:
    print("None of them are odd numbers")
else:
    print("Largest odd number",d[-1])
