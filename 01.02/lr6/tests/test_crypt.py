import pytest

from methods.crypt import Crypt

class TestCrypt:
    """
    2 TC for Crypt class

    """
    group = [
        ["BORN IN 2015!", "!4897 Oj oSpC"],
        ["99zzzabc!!!", "!!!dCbAaA00"]
    ]
    def testCase1(self):
        crypt = Crypt(self.group[0][0])
        print(crypt.first)
        assert crypt.Crypt() == self.group[0][1]
        


    def testCase2(self):
        crypt = Crypt(self.group[1][0])
        assert crypt.Crypt() == self.group[1][1]