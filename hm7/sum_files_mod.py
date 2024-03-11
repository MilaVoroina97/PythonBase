import os
from pathlib import Path
from typing import TextIO, Tuple

__all__ = ["sum_files"]

def read_first_line(file: TextIO) -> str:
    """
    Reads the first line of a file, or returns an empty string if the file is empty.
    """
    line = file.readline().strip()
    if not line:
        file.seek(0)
        line = file.readline().strip()
    return line

def sum_files(names_file: Path, numbers_file: Path, results_file: Path) -> None:
    """
    Reads two files, 'names.txt' and 'numbers.txt', and writes the results to a third file, 'results.txt'.
    Each line in 'names.txt' contains a name, and each line in 'numbers.txt' contains a pair of numbers separated by a pipe character ('|').
    The first number in each pair is an integer, and the second number is a floating-point number.
    The function multiplies the integer and floating-point numbers together, and then writes the result to 'results.txt'.
    If the result is negative, the name is written in lowercase. If the result is positive, the name is written in uppercase.
    If the result is zero, the name is not written to the file.
    """

    with open(names_file, 'r', encoding='utf-8') as f1, \
            open(numbers_file, 'r', encoding='utf-8') as f2, \
            open(results_file, 'a', encoding='utf-8') as f_res:
        num_names = sum(1 for _ in f1)
        num_numbers = sum(1 for _ in f2)
        max_lines = max(num_names, num_numbers)

        for _ in range(max_lines):
            name = read_first_line(f1)
            num_int, num_fl = read_first_line(f2).split('|')
            result = int(num_int) * float(num_fl)
            if result < 0:
                f_res.write(f"{name.lower()} {result}\n")
            elif result > 0:
                f_res.write(f"{name.upper()} {int(result)}\n")

if __name__ == "__main__":
    sum_files(Path('names.txt'), Path('numbers.txt'), Path('results.txt'))