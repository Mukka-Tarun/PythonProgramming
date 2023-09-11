#Checking for vowels in a string/name
name=input("Enter the string")
length=len(name)
i=0
while(i<length):
    if(name[i]=='A' or name[i]=='a' or name[i]=='E' or name[i]=='e' or name[i]=='I' or name[i]=='i' or name[i]=='O' or name[i]=='o' or name[i]=='U' or name[i]=='u'):
        print("Vowel=",name[i])
    else:
        print("Consonant=",name[i])
    i+=1    
