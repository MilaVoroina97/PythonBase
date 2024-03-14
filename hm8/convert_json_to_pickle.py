import json
import pickle
from pathlib import Path


__all__ = ['convert_json_to_pickle']
def convert_json_to_pickle(files_directory: Path) -> None:
    for file_obj in files_directory.iterdir():
        if file_obj.is_file() and file_obj.suffix == '.json':
            with open(file_obj, 'r', encoding='utf-8') as file_read, open(file_obj.stem + '.pickle', 'wb') as file_write:
                json_data = json.load(file_read)
                pickle.dump(json_data, file_write)

if __name__ == '__main__':
    directory_path = (Path(r'//'))
    convert_json_to_pickle(directory_path)