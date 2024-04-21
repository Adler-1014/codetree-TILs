inputs = input().split("-")
if inputs[0] != "010":
    print("첫 번째 입력은 '010'이어야 합니다.")
else:
    a, b, c = map(int, inputs)
    print(f"{a}-{c}-{b}")