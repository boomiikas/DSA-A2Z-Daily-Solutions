def print_name(name, n):
    if n == 0:
        return
    print(name)
    print_name(name, n - 1)

print_name("Boomika", 5)