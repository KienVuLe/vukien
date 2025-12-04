n = int(input("Nhập số nguyên dương n: "))

tong = 0
for i in range(n + 1):
    tong += i

print("Tổng từ 0 đến", n, "là:", tong)