import random
from pathlib import Path

__all__ = ["generate_numbers"]

MIN_NUM = -1000
MAX_NUM = 1000

def generate_numbers(num_strings: int, file_name: Path) -> None:
    """
    Generates random numbers and writes them to a file.

    The numbers are generated using the `randint()` and `uniform()` functions from the `random` module.
    The `randint()` function generates random integers within a specified range, while the `uniform()` function generates random floating-point numbers within a specified range.

    The generated numbers are written to a file in the following format:

    ```
    <integer> | <floating-point number>
    ```

    Each line of the file contains one pair of numbers.

    Args:
        num_strings (int): The number of lines to write to the file.
        file_name (Path): The path to the file to write the numbers to.
    """

    with open(file_name, 'w', encoding='utf-8') as f:
        for _ in range(num_strings):
            f.write(f"{random.randint(MIN_NUM, MAX_NUM)} | {random.uniform(MIN_NUM, MAX_NUM)}\n")


if __name__ == "__main__":
    generate_numbers(10, Path('numbers.txt'))