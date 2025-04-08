"""
 Программа загадывает число от 0 до 1000. Необходимо
 угадать число за 10 попыток. Программа должна подсказывать
 “больше” или “меньше” после каждой попытки. Для генерации
 случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
"""

# Мой код
"""
from random import randint

num = randint(1, 1000)
limit = 10  # 10 попыток (от 1 до 10)
count = 1

while count <= limit:
    j = int(input(f"Попытка {count}. Угадай число: "))

    if j < num:
        print('Твоё число меньше загаданного')
    elif j > num:
        print('Твоё число больше загаданного')
    else:
        print('Поздравляю, ты угадал!')
        break

    count += 1
else:
    print(f"Лимит попыток исчерпан. Было загадано число {num}.")
"""

# Написал DeepSeec

from random import randint

# Устанавливаем параметры игры
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10

# Генерируем случайное число
secret_number = randint(LOWER_LIMIT, UPPER_LIMIT)
attempts = 0

print(f"Я загадал число от {LOWER_LIMIT} до {UPPER_LIMIT}. Попробуй угадать его за {MAX_ATTEMPTS} попыток!")

# Основной игровой цикл
while attempts < MAX_ATTEMPTS:
    attempts += 1
    remaining_attempts = MAX_ATTEMPTS - attempts

    try:
        guess = int(input(f"Попытка {attempts}. Введи число: "))
    except ValueError:
        print("Пожалуйста, введи целое число!")
        attempts -= 1  # Не засчитываем некорректную попытку
        continue

    if guess < LOWER_LIMIT or guess > UPPER_LIMIT:
        print(f"Число должно быть между {LOWER_LIMIT} и {UPPER_LIMIT}!")
        attempts -= 1
        continue

    if guess == secret_number:
        print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток!")
        break
    elif guess < secret_number:
        print(f"Моё число больше. Осталось попыток: {remaining_attempts}")
    else:
        print(f"Моё число меньше. Осталось попыток: {remaining_attempts}")
else:
    print(f"К сожалению, ты не угадал. Я загадал число {secret_number}.")


