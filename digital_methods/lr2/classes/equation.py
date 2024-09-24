from classes.partition import Partition

class Equation:
    def __init__(self, arr_partitions):
        self.a = arr_partitions

    def solve(self, interval_part):
        resp = 0
        for x in self.a: resp += x.solve(interval_part)
        return resp
    
    def derivative(self):
        resp = []
        for x in self.a:
            if isinstance(x.derivative(), Partition): resp.append(x.derivative())
        return Equation(resp)

    def __str__(self):
        return "".join([str(x) for x in self.a])