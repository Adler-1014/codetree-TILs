n = int(input())

# Upper half
for i in range(n):
    print("*" * (n - i) + " " * (2 * i) + "*" * (n - i))