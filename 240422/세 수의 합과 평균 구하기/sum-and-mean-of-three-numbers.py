import math

arr = list(map(int, input().split()))
ans1 = sum(arr)
ans2 = ans1 / len(arr)
print(sum(arr))
print(math.floor(ans2))