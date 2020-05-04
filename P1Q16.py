#Convert capital letters to lower letters and vice versa without using built-in functions

str = input("Input the string: ")
str1 = '';
for a in str:
    if a.isupper():
        str1 = str1 + (a.lower())
    elif a.islower():
        str1 = str1 + (a.upper())

print("Case CHanged String :" + str1)
