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
