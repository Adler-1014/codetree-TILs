n = int(input())
ans = ''

if n < 1000:
    ans = 'no'
elif n >= 3000:
    ans = 'book'
else:
    ans = 'mask'

print(ans)