a = input("enter the string:")

count =0

for i in a:
    if i in "aeiouAEIOU":
        count+= 1
        
print("vowels=",count)        
    
