a_age,a_gen = map(int,input().split())
b_age,b_gen = map(int,input().split())


if (a_age >= 19 and a_gen == 'M') OR (b_age >=19 and b_gen == 'M'):
    print(1)
else:
    print(0)