import pytest

from methods.dnk import DNK


class TestDNK:
    """
        5 of 7, from first
    """
    group = [
        ["TTTT", "UUUU"],
        ["GCAT", "GCAU"],
        ["GACCGCCGCC", "GACCGCCGCC"],
        ["GATTCCACCGACTTCCCAAGTACCGGAAGCGCGACCAACTCGCACAGC", "GAUUCCACCGACUUCCCAAGUACCGGAAGCGCGACCAACUCGCACAGC"],
        ["CACGACATACGGAGCAGCGCACGGTTAGTACAGCTGTCGGTGAACTCCATGACA", "CACGACAUACGGAGCAGCGCACGGUUAGUACAGCUGUCGGUGAACUCCAUGACA"],
    ]
    def testCase1(self):
        dnk = DNK(self.group[0][0])
        assert dnk.GiveRNK() == self.group[0][1]

    def testCase2(self):
        dnk = DNK(self.group[1][0])
        assert dnk.GiveRNK() == self.group[1][1]

    def testCase3(self):
        dnk = DNK(self.group[2][0])
        assert dnk.GiveRNK() == self.group[2][1]

    def testCase4(self):
        dnk = DNK(self.group[3][0])
        assert dnk.GiveRNK() == self.group[3][1]

    def testCase5(self):
        dnk = DNK(self.group[4][0])
        assert dnk.GiveRNK() == self.group[4][1]