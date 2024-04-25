n = int(input())

# Upper half
for i in range(n):
    print("*" * (i + 1))
    print()

# Lower half
for i in range(n - 1, 0, -1):
    print("*" * i)
    print()