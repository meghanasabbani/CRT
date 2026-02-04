'''for i in range(1,11):
    if i == 5:
        continue
    print(i,end=" ")  
'''
m="meghana007@5"
for i in range(3):
    n=input("Enter password:")
    if n==m:
        print("login successful")
        break
else:
    print("Account locked")