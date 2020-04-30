str1= str(input("Enter string 1: "))
str2= str(input("Enter string 2: "))
def isIn(str1,str2):
    if ((str1 in str2) or (str2 in str1)):
        return True
    else:
        return False
print(isIn(str1,str2))
