import json
import os


# загружаем файл, проверяем, что он существует.

def load_data(filepath):
    if not os.path.exists(filepath):
        return print("Ошибка чтения файла. Проверьте его наличие по заданному пути")
    else:
        with open(filepath, 'r', encoding='UTF-8') as work_file:
            return json.load(work_file)


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    file_path = input("Введите имя и путь до файла:")
    json_file_content = load_data(file_path)
    if json_file_content:
        pretty_print_json(json_file_content)
    else:
        print('Данные не загруженны. Попробуйте еще раз')