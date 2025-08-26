#Write a function that takes a list and appends an element to it. Check the list inside and outside the function.
def list_append(arr):
    n=len(arr)/2
    arr.append(n)
    print("Inside the function:",arr)

arr=eval(input())  
list_append(arr)
print("Outside the function:",arr)