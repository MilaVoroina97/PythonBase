# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.


import random
list = [random.randint(0, 10) for _ in range(20)]
print(list)

new_list = []
for item in set(list):
    if list.count(item) > 1:
        new_list.append(item)
print(new_list)