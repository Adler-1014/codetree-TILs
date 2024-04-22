a = int(input())
ans = 0
if a % 2 != 0 :
    ans = a + 3
    if ans % 3 == 0:
        ans %= 3

print(ans)