#without function
str=input("enter you're string:"
          )
count=0
str1=""
for ch in str:
    count=count+1
    str1=ch+str1
print("given string is:",count)

if(str==str1):
    print("given string is palindrome")

elif(str!=str1):
    print("given string is not palindrome")
    print("the revers string is:",str1)