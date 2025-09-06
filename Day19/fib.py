n=int(input())
a=0
b=1
print("Fibonacci series upto ",n,"terms:")
for i in range(n):
    print(a,end=" ")
    c=a+b 
    a=b
    b=c