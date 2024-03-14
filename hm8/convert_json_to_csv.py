import csv
import json
from pathlib import Path


__all__ = ['convert_json_to_csv']
def convert_json_to_csv(file_path: Path) -> None:
    # Чтение данных из JSON файла
    with open(file_path, 'r', encoding='utf-8') as file_read:
        json_data = json.load(file_read)

    # Преобразование данных в формат для CSV
    csv_data = []
    for level, id_name in json_data.items():
        for user_id, user_name in id_name.items():
            csv_data.append({'level': int(level), 'id': int(user_id), 'name': user_name})

    # Запись данных в CSV файл
    csv_file_path = file_path.stem + ".csv"
    with open(csv_file_path, 'w', encoding='utf-8', newline='') as file_write:
        csv_writer = csv.DictWriter(file_write, fieldnames=['level', 'id', 'name'])
        csv_writer.writeheader()
        csv_writer.writerows(csv_data)

if __name__ == '__main__':
    # Выполнение функции для преобразования JSON в CSV
    json_file_path = Path('users.json')
    convert_json_to_csv(json_file_path)