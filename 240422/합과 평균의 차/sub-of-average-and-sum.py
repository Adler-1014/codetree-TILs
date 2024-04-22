arr = list(map(int,input().split()))
ans1 = sum(arr)
ans2 = sum(arr) / len(arr)
ans3 = ans1-ans2

print(ans1)
print(int(ans2))
print(int(ans3))