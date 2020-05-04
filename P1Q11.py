#To Check if two different strings has the same letters (Anagram)

str1=str(input("Enter the 1st string: "))
str2=str(input("Enter the second string: "))

sort1= sorted(str1)
sort2= sorted(str2)

if sort1==sort2 :
    print("It is an Anagram! ")
else :
    print("It is not an Anagram")


