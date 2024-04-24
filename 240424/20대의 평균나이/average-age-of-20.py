arr = []

while True: 
    n = int(input())
    if 20<= n < 30:
        arr.append(n)
    else:
        break
ans = sum(arr) / len(arr)
print(f"{ans:.2f}")