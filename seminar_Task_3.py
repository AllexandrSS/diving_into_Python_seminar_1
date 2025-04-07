while True:
    a = int(input('Введите число от 1 до 999: '))
    if 1 <= a <= 999:
        break

if a < 10:
    print(a**2)
elif a < 100:
    print((a % 10) * (a // 10))
else:
    print(f"{a % 10}{a // 10 % 10}{a // 100}")
    print(str(a)[:: -1])   # решение через строку