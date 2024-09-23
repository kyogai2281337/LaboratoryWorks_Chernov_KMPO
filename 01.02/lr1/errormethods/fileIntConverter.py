import sys
from general.IOfuncs import *

"""
Ошибка в преобразовании, мы её не обработали верным образом.
Для того, чтобы её исправить, необходимо добавить проверку вводных данных.
"""
def main():
    if len(sys.argv) > 1 and sys.argv[1].endswith('.txt'):
        data = read_data_from_file(sys.argv[1])
    else:
        data = read_data_from_command_line()

    #PLACE OF ERROR
    data = int(data)  # попытка преобразовать данные в целое число
    """
        data = int(data)  # попытка преобразовать данные в целое число
           ^^^^^^^^^
    ValueError: invalid literal for int() with base 10: 'asdf'
    """

    print(f"Входные данные: {data}")

if __name__ == "__main__":
    main()