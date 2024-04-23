a = int(input())

for i in range(1, a + 1):
    if i % 2 == 0 and i % 4 != 0:
        continue
    ans1 = i // 8
    if ans1 % 2 == 0:
        continue
    ans2 = i % 7
    if ans2 < 4:
        continue
    print(i,end= " ")