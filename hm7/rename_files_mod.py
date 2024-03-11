# Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import random
import string
import os

__all__ = ['rename_group']

def generate_random_files(count: int):
    file_extensions = ['txt', 'jpg', 'mov', 'mp3', 'bin', 'csv', 'md', 'doc']
    for _ in range(count):
        name = ''.join(random.sample(string.ascii_lowercase, 10)) + '.' + random.choice(file_extensions)
        with open(name, 'w', encoding='utf-8') as file:
            file.write(name)

def rename_group(directory: str = os.getcwd(),
                 new_prefix: str = '',
                 digit_count: int = 1,
                 input_extension: str = '',
                 output_extension: str = '___',
                 range_limits: tuple = (0, 10)):
    file_count = 1
    if os.path.isdir(directory):
        for file in os.listdir(directory):
            file_name, file_extension = os.path.splitext(file)
            if file_extension == input_extension or not input_extension:
                renamed_file = (f'{file_name[range_limits[0]:range_limits[1]]}'
                                f'{new_prefix if new_prefix else ""}'
                                f'{file_count:0>{digit_count}}.{output_extension}')
                os.rename(os.path.join(directory, file), os.path.join(directory, renamed_file))
                file_count += 1
        print(f'Переименовано {file_count - 1} файлов.')
    else:
        print('Указанный путь не является директорией.')

if __name__ == '__main__':
    rename_group(new_prefix='new', input_extension='txt', output_extension='jpeg', digit_count=5, range_limits=(2, 7))