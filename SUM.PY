n=int(input("enter your num:"))
total=0
while n>0:
    digit=n%10
    total=total+digit
    n=n//10
print("total=",total)
