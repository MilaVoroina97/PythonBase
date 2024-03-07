# В модуль с проверкой даты добавьте возможность запуска в терминале
# с передачей даты на проверку.

import sys

def is_leap_year(year):
    # Проверяет, является ли год високосным
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def validate_date(date_str):
    try:
        day, month, year = map(int, date_str.split('.'))
    except ValueError:
        return False

    # Словарь для хранения максимального количества дней в каждом месяце
    max_days_in_month = {
        1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31,
        4: 30, 6: 30, 9: 30, 11: 30,
        2: 29 if is_leap_year(year) else 28
    }

    # Проверка правильности года, месяца и дня
    if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1 or day > max_days_in_month[month]:
        return False

    return True

if __name__ == '__main__':
    date_str = sys.argv[1]
    result = validate_date(date_str)
    print(result)