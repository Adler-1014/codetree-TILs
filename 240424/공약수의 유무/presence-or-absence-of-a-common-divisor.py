a,b = map(int,input().split())

cd = []

for i in range (1,1920):
    if (1920 % i == 0) and (2880 % i == 0):
        cd.append(i)
ans = 0
for i in range(a,b+1):
    if i in cd:
        ans = 1
        break
    else:
        print(0)

print(ans)