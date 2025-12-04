import math

print("Giải phương trình bậc 2: ax^2 + bx + c = 0")
s = input("Nhập a b c (cách nhau bằng khoảng trắng): ")
a, b, c = map(float, s.split())

if a == 0:
    print("Đây không phải phương trình bậc 2.")
else:
    delta = b**2 - 4*a*c

    if delta < 0:
        print("Phương trình vô nghiệm.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép x = {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có 2 nghiệm phân biệt:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")