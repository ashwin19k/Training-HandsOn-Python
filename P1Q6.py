my_string = str(input("Enter the string: "))
my_list = my_string.split(",")
sum_my_list = 0;
for i in my_list :
    sum_my_list += float(i)
print(sum_my_list)
