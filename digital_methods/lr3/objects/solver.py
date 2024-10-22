from objects.equation import Equation

class Solver:
    def __init__(self, equation, interval):
        self.equation = equation
        self.interval = interval
    def solve(self):
        return self.equation.solve(self.interval_part)