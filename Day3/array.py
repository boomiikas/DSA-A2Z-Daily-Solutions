#Count how many even numbers are in a list.
arr=eval(input())
c=0
for i in range(len(arr)):
    if(arr[i]%2==0):
        c+=1
print("Count_even:",c)
