n = int(input())
ans = []
for i in range(n):
    num = int(input())
    if num % 2 != 0 and num % 3 == 0:
        ans.append(num)

for i in ans:
    print(i)