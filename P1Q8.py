n = int(input("Enter the number of intergers = "))
vector1 = []
vector2 = []

for i in range(0,n) :
    v1= int(input("Enter vector 1 values : "))
    vector1.append(v1)

for i in range(0,n) :
    v2 = int(input("Enter vector 2 values : "))
    vector2.append(v2)


e =[]
try:
    for x in range(0,len(vector1)):
        if vector1[x] / vector2[x] != 0:
            e.append(vector1[x] / vector2[x])

        else:
            raise Exception('Exception')
    print(e)

except:
    print("An exception occurred")

