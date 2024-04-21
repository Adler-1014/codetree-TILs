inputs = input().split("-")
if inputs[0] != "010":
    print("첫 번째 입력은 '010'이어야 합니다.")
else:
    a = inputs[0]
    b,c =inputs[1],inputs[2]
    print(f"{a}-{c}-{b}")