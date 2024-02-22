#Напишите программу, которая принимает две строки вида “a/b” - дробь с
# числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions

import fractions

fraction_1 = input("Введите первую дробь (в виде a/b): ").split('/')
fraction_2 = input("Введите вторую дробь (в виде a/b): ").split('/')

numerator_sum = int(fraction_1[0]) * int(fraction_2[1]) + int(fraction_2[0]) * int(fraction_1[1])
denominator_sum = int(fraction_1[1]) * int(fraction_2[1])
sum_fractions = [numerator_sum, denominator_sum]

multi_fractions = [int(fraction_1[0]) * int(fraction_2[0]), int(fraction_1[1]) * int(fraction_2[1])]

a_1, b_1 = sum_fractions
while b_1:
    a_1, b_1 = b_1, a_1 % b_1

a_2, b_2 = multi_fractions
while b_2:
    a_2, b_2 = b_2, a_2 % b_2

result_sum = (f'{sum_fractions[0] // a_1}/{sum_fractions[1] // a_1}')
result_multi = (f'{multi_fractions[0] // a_2}/{multi_fractions[1] // a_2}')

print(f'Сумма =  {result_sum}')
print(f'Результат умножения = {result_multi}')

fraction_1_F = fractions.Fraction(f'{fraction_1[0]}/{fraction_1[1]}')
fraction_2_F = fractions.Fraction(f'{fraction_2[0]}/{fraction_2[1]}')

result_sum_F = fraction_1_F + fraction_2_F
result_multi_F = fraction_1_F * fraction_2_F

print('After fraction:')

print(f'Сумма = {result_sum_F}')
print(f'Результат умножения =  {result_multi_F}')

if str(result_sum) == str(result_sum_F) or str(result_multi) == str(result_multi_F):
    print('Результаты верны.')
else:
    print('Возникла ошибка. Попробуйте еще.')