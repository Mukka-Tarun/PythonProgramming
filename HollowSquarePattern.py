#Program for Hollow Square Pattern
row=int(input("Enter the number of rows"))
print("Hollow square pattern is:")
for i in range(1,row+1):
    for j in range(1,row+1):
        if i==1 or i==row or j==1 or j==row:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()             

