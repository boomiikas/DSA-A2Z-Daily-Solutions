def print_n_times(n):
    if n == 0:     
        return
    print("Hello")
    print_n_times(n - 1) 
n=int(input())
print_n_times(n)