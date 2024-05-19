a=int(input("Enter a positive integer number= "))

if a%3 == 0 and a%7!=0:
    print("Multiply by 3")
elif a%7==0 and a%3!=0:
    print("Multiply by 7")
elif a%7==0 and a%3==0:
    print("Multiply by 3 and 7 both")
else:
    print("Not multiply by 3 or 7 or both")