import os
import json
import csv
import pickle
from pathlib import Path

__all__ = ['explore_directory']

def explore_directory(path: Path) -> None:
    data_list = []

    for current_root, directories, files in os.walk(path):
        total_size = 0

        for current_file in files:
            file_path = os.path.join(current_root, current_file)
            file_size = os.path.getsize(file_path)
            total_size += file_size
            data_list.append({
                'path': file_path,
                'file_type': 'file',
                'file_size': file_size,
                'parent_directory': current_root
            })

        for directory_name in directories:
            dir_path = os.path.join(current_root, directory_name)
            total_size += calculate_directory_size(dir_path)
            data_list.append({
                'path': dir_path,
                'file_type': 'directory',
                'directory_size': total_size,
                'parent_directory': current_root
            })

    save_to_json_file(data_list, 'output.json')
    save_to_csv_file(data_list, 'output.csv')
    save_to_pickle_file(data_list, 'output.pkl')


def calculate_directory_size(path):
    total_size = 0

    for current_path, dirs, files in os.walk(path):
        for current_file in files:
            file_path = os.path.join(current_path, current_file)
            total_size += os.path.getsize(file_path)

    return total_size


def save_to_json_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def save_to_csv_file(data, filename):
    headers = ['path', 'file_type', 'file_size', 'parent_directory']
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


def save_to_pickle_file(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


if __name__ == '__main__':
    explore_directory(r'C:\Users\ASUS\IdeaProjects\PythonBase\hm8')