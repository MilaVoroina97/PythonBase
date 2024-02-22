# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток. Программа должна
# подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num_to_guess = randint(LOWER_LIMIT, UPPER_LIMIT)

for _ in range(10):
    guess = int(input(f"Угадайте число от {LOWER_LIMIT} до {UPPER_LIMIT}: "))

    if guess < num_to_guess:
        print("Больше")
    elif guess > num_to_guess:
        print("Меньше")
    else:
        print("Поздравляем, вы угадали число!")
        break
else:
    print(f"Вы исчерпали все попытки. Загаданное число было: {num_to_guess}")
