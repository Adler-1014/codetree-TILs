n = int(input())
temp = 11
# n번 반복
for i in range(n):
    for j in range(n):
        print(temp+2*j, end = " ")
    
    temp += 2
    print()