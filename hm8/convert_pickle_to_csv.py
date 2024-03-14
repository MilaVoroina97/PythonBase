import csv
import pickle
from pathlib import Path


__all__ = ['convert_pickle_to_csv']
def convert_pickle_to_csv(file_path: Path) -> None:
    with open(file_path, 'rb') as file_read:
        data = pickle.load(file_read)

    headers = list(data[0].keys())
    with open(file_path.stem + '.csv', 'w', newline='', encoding='utf-8') as file_write:
        csv_writer = csv.DictWriter(file_write, fieldnames=headers, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        csv_writer.writerows(data)

if __name__ == '__main__':
    pickle_file_path = Path('new_user.pickle')
    convert_pickle_to_csv(pickle_file_path)