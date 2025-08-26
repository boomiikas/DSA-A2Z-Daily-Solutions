#Write a function that takes a string and converts it to uppercase inside the function. Print the string inside and outside.
def upper(s):
    t=str.upper(s)
    print("Inside the function call :",t)
s=input()
upper(s)
print("Outside the function call :",s)