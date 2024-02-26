# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.


from itertools import chain, combinations

hike = {'Кружка': 1.0,
        'Палатка': 10.0,
        'Полотенце': 2.0,
        'Сухпаек': 6.0,
        'Вода': 5.0,
        'Дрова': 10.5,
        'Карта': 0.5

        }

capacity = int(input('Грузоподъёмность рюкзака: '))
backpack = 0
pack = []

for thing, weight in hike.items():
    if backpack + weight <= capacity:
        backpack += weight
        pack.append(thing)
pack.append(backpack)
print(pack)