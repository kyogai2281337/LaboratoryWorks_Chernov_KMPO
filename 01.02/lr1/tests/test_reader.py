import sys
from general.IOfuncs import *
import pytest


def test_reader():
    if len(sys.argv) > 1 and sys.argv[1].endswith('.txt'):
        data = read_data_from_file(sys.argv[1])
    else:
        data = "asdf"

    try:
        data = int(data)
    except ValueError:
        print("Некорректные входные данные. Входные данные должны быть целым числом.")
        return

    print(f"Входные данные: {data}")
    assert True