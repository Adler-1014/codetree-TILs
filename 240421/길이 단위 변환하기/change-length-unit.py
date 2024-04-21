a_ft = 9.2


b_mi = 1.3

def convert_ft_to_cm(ft:float):
    
    a_cm = round(ft * 30.48,1)
    return a_cm

def convert_mi_to_cm(mi:float):
    b_cm = round(mi * 160934,1)
    return b_cm

ans1,ans2 = convert_ft_to_cm(a_ft), convert_mi_to_cm(b_mi)

print(f"{a_ft}ft = {ans1}cm")
print(f"{b_mi}mi = {ans2}cm")