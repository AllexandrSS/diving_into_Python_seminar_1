n = int(input('Введите число: '))
e = int(input('Введите ещё одно число: '))
count = 2
sum1 = 0
while count <= n:
    if count % e == 0:
        count += 2
        continue
    sum1 += count
    count += 2
    print(sum1)
print(sum1)