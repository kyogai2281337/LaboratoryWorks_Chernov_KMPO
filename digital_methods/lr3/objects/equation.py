from objects.partition import Partition

class Equation:
    def __init__(self, arr_partitions):
        self.a = arr_partitions

    def solve(self, interval_part):
        pass
    
    def derivative(self):
        resp = []
        for x in self.a:
            if isinstance(x.derivative(), Partition): resp.append(x.derivative())
        return Equation(resp)
    
    def inderivative(self):
        resp = []
        for x in self.a:
            if isinstance(x.inderivative(), Partition): resp.append(x.inderivative())
        return Equation(resp)

    def __str__(self):
        return "".join([str(x) for x in self.a])