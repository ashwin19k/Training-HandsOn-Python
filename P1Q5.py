root =int(input("Enter an integer ="))

for pwr in range(1,5):

    if root**pwr == root:
        print ("Match found - root,pwr=", root,pwr)

    else:
        pwr += 1
        print ("Match not found - root,pwr=",root, pwr)
