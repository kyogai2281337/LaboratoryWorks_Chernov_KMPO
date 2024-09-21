# Лабораторная работа №6. Знакомство с Pytest

## Цель работы, Задачи
Цель - научиться использовать pytest на базовом уровне.

Задачи:
1. Научиться базовым навыкам работы с Pytest.
2. [Разработать алгоритмы для работы с Pytest.](#код)
3. [Вызов тестов](#тесты)
4. Вывод

---

## Код
Все реализации методов и обьектов находятся в папке __./methods__
```python
# dnk.py
"""
    Задача:
    - func() self.dnkstr -> rnkstr (T -> U)
"""


class DNK:
    # Initialization
    dnkstr = ""
    def __init__(self, dnkstr):
        self.dnkstr = dnkstr

    # DNK -> RNK
    def GiveRNK(self):
        if len(self.dnkstr) == 0:
            return EOFError
        resp = ""
        for l in range(len(self.dnkstr)):
            letter = self.dnkstr[l]
            if letter == 'T':
                resp += 'U'
                continue
            resp += letter

        return resp
```
```python
# crypt.py
import string

class Crypt:
    # Initialization
    first = ""
    alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    def __init__(self, first):
        self.first = first.lower()

    # cryptstr
    def Crypt(self):
        if len(self.first) == 0:
            return ValueError("Входная строка пуста")

        resp = ""
        iter = 0
        for el in self.first:
            if el in self.alphabet:
                # Find the next letter in the alphabet
                next_index = (self.alphabet.index(el) + 1) % len(self.alphabet)
                next_char = self.alphabet[next_index]

                if iter == 0 or iter % 2 == 0:
                    resp += next_char.upper()
                else:
                    resp += next_char
                iter += 1
                continue

            elif el in self.digits:
                resp += str(9 - int(el)) if el != '0' else '9'
                iter += 1
                continue

            iter += 1
            resp += el

        return resp[::-1]

```

## Тесты
Все реализации тестов находятся в папке __./tests__. Для определённой части тестов решил использовать классовое определение с singleton-методами, для упрощения работы с определением точек ошибок и увеличения читаемости текста.

### IDE

#### VSCode
Я использую VSCode, т.к. Python - не мой стек, в следствии чего, все мои настройки-pathfinder-ы располагаются в директории __./vscode__.
#### PyCharm
Для пользователей PyCharm linter автоматически определит папки, в которых находятся тесты.
#### Bash/Vim/Neovim...
Команда для запуска тестов:
```bash
pytest <flags_if_needed>
```

## Вывод
Я научился использовать Pytest на базовом уровне!!! 

## P.S. 
Могу ли я создать репозиторий для работы с ЛР, которые вы будете задавать? будет удобно и мне, и вам, т.к. не придётся постоянно хранить реестр данных на локальной машине, а запуски всех тестов буду пробрасывать через GitHub Actions, чтобы вы смогли увидеть результаты тестов не запуская скрипты.