a=int(input("Enter the length of the list"))
mylist=[]
for i in range(a):
    b=(input("Enter {} number index value".format(i)))
    mylist.append(b)
print("Entered list is= ",mylist)
print("Reverse of the list is= ",mylist[::-1])