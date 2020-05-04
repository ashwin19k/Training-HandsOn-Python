#Sort list with alternative increasing and decreasing order [7,1,9,2,4,6,8,3] -> [1,9,2,8,3,7,4,6]

def sortList(numList):
    numList.sort()
    print(numList)
    sort_list=[]
    i=0
    j=len(numList) -1
    while i < len(numList) and j > -1 and i < j :
        sort_list.append(numList[i])
        sort_list.append(numList[j])
        i=i+1
        j=j-1
    if len(numList) % 2 != 0 :
        sort_list.append(numList[i])
    return sort_list

input_list=[9,3,2,6,5,7,1,4,8]
print("The original list is :", input_list)
print("The sorted list is ", sortList(input_list))

