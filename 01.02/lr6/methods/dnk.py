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