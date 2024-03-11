import random
from pathlib import Path

__all__ = ['generate_names']

MINIMUM_LENGTH = 4
MAXIMUM_LENGTH = 7
VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'

def generate_names(name_count: int, file_path: str | Path) -> None:
    with open(file_path, 'a', encoding='utf-8') as file:
        for _ in range(name_count):
            name = ''
            direction = random.choice([-1, 1])
            for _ in range(random.randint(MINIMUM_LENGTH, MAXIMUM_LENGTH)):
                if direction == -1:
                    name += random.choice(CONSONANTS)
                else:
                    name += random.choice(VOWELS)
                direction *= -1
            file.write(name.title() + '\n')

if __name__ == '__main__':
    generate_names(10, Path('../names.txt'))