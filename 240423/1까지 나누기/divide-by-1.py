n = int(input())
cnt = 1
for i in range(1,n+1):
    n = n // i
    if n <= 1:
        break
    cnt +=1 
   
print(cnt)