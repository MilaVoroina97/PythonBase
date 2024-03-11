import random
import string
import os
from pathlib import Path


__all__ = ['generate_files', 'organize_files']

# Функция для создания случайных файлов
def create_diverse_files(file_directory: Path, file_types: dict[str, int]) -> None:
    os.chdir(file_directory)  # Переход в указанный каталог
    for file_type, file_count in file_types.items():
        generate_files(file_type, file_count)  # Генерация файлов для каждого типа

# Функция для сортировки файлов по расширениям
def organize_files(directory: Path, file_categories: dict[Path, list[str]]) -> None:
    os.chdir(directory)  # Установка рабочего каталога
    # Создаем словарь соответствий расширений и целевых каталогов
    extension_to_category = {}
    for category, extensions in file_categories.items():
        for extension in extensions:
            extension_to_category[extension] = category
    # Сортировка файлов по расширениям
    for file in directory.iterdir():
        if file.is_file() and file.suffix in extension_to_category:
            file.replace(extension_to_category[file.suffix] / file.name)  # Перемещение файла в соответствующий каталог

# Функция для генерации файлов случайного размера и содержания
def generate_files(extension: str, file_count: int) -> None:
    for _ in range(file_count):
        while True:
            # Генерация уникального имени файла
            file_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(6, 30)))
            # Проверка, не существует ли файл с таким именем
            if not Path(f'{file_name}.{extension}').exists():
                break
        # Генерация случайных данных для файла
        file_size = random.randint(256, 4096)
        file_data = bytes(random.getrandbits(8) for _ in range(file_size))
        # Сохраняем файл
        with open(f'{file_name}.{extension}', 'wb') as file:
            file.write(file_data)

# Выполнение кода
if __name__ == '__main__':
    spam_directory = Path('/Package/test/spam')
    spam_directory.mkdir(parents=True, exist_ok=True)  # Создаем каталог для файлов, если он не существует
    file_types = {'avi': 1, 'jpeg': 1, 'mkv': 1, 'png': 1}  # Определяем типы файлов и их количество
    create_diverse_files(spam_directory, file_types)  # Генерируем случайные файлы

    file_categories = {
        Path('video'): ['avi', 'mov', 'mkv', 'mk4'],
        Path('images'): ['bmp', 'jpeg', 'jpg', 'png']
    }  # Определяем категории файлов и соответствующие расширения
    organize_files(spam_directory, file_categories)  # Сортируем файлы по категориям

