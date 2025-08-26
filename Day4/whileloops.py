#Keep printing squares of numbers until the square exceeds 100.

n=int(input())
while(n*n<100):
    print(n*n,end=" ")
    n+=1