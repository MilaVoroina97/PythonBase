import json
import csv
from pathlib import Path

__all__ = ['convert_csv_to_json']
def convert_csv_to_json(input_path: Path, output_path: Path) -> None:
    data_list = []
    with open(input_path, 'r', encoding='utf-8', newline='') as file_read:
        csv_reader = csv.reader(file_read, dialect='excel-tab')
        for idx, row in enumerate(csv_reader):
            if idx != 0:
                level, user_id, user_name = row
                data = {
                    "level": int(level),
                    "id": f'{int(user_id):010}',
                    "name": user_name.title(),
                    "hash": hash(f'{user_name.title()}{int(user_id):010}')
                }
                data_list.append(data)

    with open(output_path, 'w', encoding='utf-8') as file_write:
        json.dump(data_list, file_write, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    input_file_path = Path('users.csv')
    output_file_path = Path('new_user.json')
    convert_csv_to_json(input_file_path, output_file_path)