n = int(input())
temp = 1

for i in range(n):
    for j in range(n,0,-1):
        print(temp*j, end = " ")
    temp +=1 
    print()