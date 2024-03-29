# Напишите код, который запрашивает число и сообщает
# является ли оно простым или составным. Используйте правило для
# проверки: “Число является простым, если делится нацело
# только на единицу и на себя”. Сделайте ограничение на ввод
# отрицательных чисел и чисел больше 100 тысяч.

def check_prime(num):
    if num <= 1 or num > 100000:
        return "Число должно быть больше 1 и не больше 100000"

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "Число составное"

    return "Число простое"

num = int(input("Введите число: "))
result = check_prime(num)
print(result)