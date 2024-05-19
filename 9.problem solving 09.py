a=int(input("Enter the length of the list= "))
mylist=[]
for i in range(a):
    b=int(input("Enter {} number index value: ".format(i)))
    mylist.append(b)
print("Entered list is= ",mylist)

for i in mylist:
    if (5 in mylist) and (3 in mylist):
    
        print("5 and 3 found in the list")
        break
    else:
    
        print("5 and 3 not found in the list")
        break
