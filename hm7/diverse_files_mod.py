import random
import string
import os
from pathlib import Path

__all__ = ['generate_diverse_files']

def generate_files(extension: str, min_name_length: int=6, max_name_length: int=30, min_file_size: int=256,
                   max_file_size: int=4096, file_quantity: int=42) -> None:
    for _ in range(file_quantity):
        while True:
            file_name = ''.join(random.choices(string.ascii_lowercase + string.digits + '_', k=random.randint(min_name_length, max_name_length)))
            if not os.path.isfile(f'{file_name}.{extension}'):
                break
        file_data = bytes(random.randint(0, 255) for _ in range(random.randint(min_file_size, max_file_size)))
        with open(f'{file_name}.{extension}', 'wb') as file:
            file.write(file_data)


def generate_diverse_files(directory: str | Path, **kwargs) -> None:
    if isinstance(directory, str):
        directory = Path(directory)
    if not directory.is_dir():
        directory.mkdir(parents=True)
    os.chdir(directory)
    for file_extension, file_count in kwargs.items():
        generate_files(file_extension, file_count=file_count)

if __name__ == '__main__':
    #generate_files('bin', file_count=2)
    generate_diverse_files('/test/spam', bin=1, jpeg=1)