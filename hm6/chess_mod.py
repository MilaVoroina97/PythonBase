# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
# определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину,
# а если бьют - ложь.

# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.


import random

def check_attack(x1, y1, x2, y2):
    # Проверяет, могут ли две фигуры атаковать друг друга по горизонтали, вертикали или диагонали
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

def validate_positions(positions):
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            x1, y1 = positions[i]
            x2, y2 = positions[j]
            if check_attack(x1, y1, x2, y2):
                return False
    return True

def generate_random_positions():
    valid_positions = []
    while len(valid_positions) < 8:
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        if (x, y) not in valid_positions:
            valid_positions.append((x, y))
    return valid_positions

if __name__ == '__main__':
    successful_attempts = 0
    while successful_attempts < 4:
        random_positions = generate_random_positions()
        result = validate_positions(random_positions)
        if result:
            successful_attempts += 1
            print(f'Успешная расстановка {random_positions}')