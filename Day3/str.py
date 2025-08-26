#Check if a string is a palindrome.
str=input()
if(str==str[::-1]):
    print(str,"is a palindrome")
else:
    print(str,"is not a palindrome")