arr = list(map(int, input().split()))
ans1 = sum(arr)
ans2 = sum(arr) / len(arr)
print(sum(arr))
print(f"{ans2}:.1f")