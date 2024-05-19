a=int(input("Enter a non negative integer number"))
b=int(input("Enter a non negative integer number"))
first=a%10
second=b%10


if first == second:
    print("The rightmost digit is same")
else:
    print("The rightmost digit is same not same")