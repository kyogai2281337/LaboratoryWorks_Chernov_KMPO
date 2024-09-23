import sys

def read_data_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")
        return None

def read_data_from_command_line():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return input("Введите данные: ")