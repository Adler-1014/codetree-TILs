arr = []
for i in range(5):
    n = int(input())
    arr.append(n)
cnt = 0
for i in arr:
    if i % 3 == 0:
        cnt +=1
    

if cnt == 5:
    print(1)
else:
    print(0)