import csv
import pickle
from pathlib import Path

__all__ = ['convert_csv_to_pickle']
def convert_csv_to_pickle(file_path: Path) -> None:
    with open(csv_file_path, 'r', encoding='utf-8', newline='') as file_read:
        csv_reader = csv.reader(file_read, dialect='excel')
        data_list = []
        for idx, row in enumerate(csv_reader):
            if idx != 0:
                data_list.append(dict(zip(headers, row)))
            else:
                headers = row

    print(pickle.dumps(data_list))

if __name__ == '__main__':
    csv_file_path = Path('new_user.csv')
    convert_csv_to_pickle(csv_file_path)