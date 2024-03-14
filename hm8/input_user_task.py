from pathlib import Path
import json

__all__ = ['manage_user_data']

def manage_user_data(file_path: Path) -> None:
    user_ids = set()
    if not file_path.is_file():
        data = {str(level): {} for level in range(1, 8)}
    else:
        with open(file_path, 'r', encoding='utf-8') as file_read:
            data = json.load(file_read)
            for id_name in data.values():
                user_ids.update(id_name.keys())

    while user_name := input('Enter user name: '):
        level = input('Enter level from 1 to 7: ')
        user_id = input('Enter user ID: ')
        if user_id not in user_ids:
            user_ids.add(user_id)
            data[level].update({user_id: user_name})
            with open(file_path, 'w', encoding='utf-8') as file_write:
                json.dump(data, file_write, indent=4, ensure_ascii=False)
        else:
            print('User with such ID already exists!')


if __name__ == '__main__':
    manage_user_data(Path('users.json'))