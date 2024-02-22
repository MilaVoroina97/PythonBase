#Напишите программу, которая получает целое число и возвращает его
#шестнадцатеричное строковое представление.Функцию hex используйте для
#проверки своего результата.

HEX_ALPHA = '0123456789ABCDEF'
BASE = 16

number = int(input("Введите целое число: "))
original = number

result = ''
while number > 0:
    result = HEX_ALPHA[number % BASE] + result
    number //= BASE

print(f'Число {original} в {BASE}-чной системе будет {result.lower()}')
print(f'hex({original}) = {hex(original)[2:]}')

if result.lower() == hex(original)[2:]:
    print('Результат верный')
else:
    print('Возникла ошибка. Попробуйте еще раз')