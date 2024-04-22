a = float(input())
ans = ''
if a > 1.0:
    ans = 'High'
elif a < 0.5 :
    ans = 'Middle'
else:
    ans = 'Low'

print(ans)