

class Solver:
    def __init__(self, func, interval, target=0.1):
        self.func = func
        self.derivative1 = self.func.derivative()
        self.derivative2 = self.derivative1.derivative()
        self.interval = interval
        self.target = target
        self.cycle = -1

    def find_roots(self):
        func_roots = self.func.solve(self.interval[0]), self.func.solve(self.interval[1])
        derivative1_roots = self.derivative1.solve(self.interval[0]), self.derivative1.solve(self.interval[1])
        derivative2_roots = self.derivative2.solve(self.interval[0]), self.derivative2.solve(self.interval[1])
        return [func_roots, derivative1_roots, derivative2_roots]

    def is_route_here(self):
        arr = self.find_roots()
        # f f1 f2; 1) f(m)*f(s)<0; 2) f1(avg)*f2(avg)>0
        resp = []
        for el in arr:
            if el[0]*el[1] < 0:
                resp.append(True)
            else:
                resp.append(False)
        return True if resp[0] and resp[1] == resp[2] else False

    
    def segment_interval(self):
        return self.interval[0]+(self.interval[1]-self.interval[0])/2

    def solve(self):
        self.cycle += 1
        
        # Ограничение на количество рекурсий
        if self.cycle > 1000:
            raise RecursionError("Превышена максимальная глубина рекурсии. Проверьте интервал и функцию.")
        
        # Проверка, удовлетворяет ли текущий интервал целевому значению
        if abs(self.interval[1] - self.interval[0]) < self.target:
            return str(self)
        
        mid_point = self.segment_interval()
        
        # Создаем два новых подынтервала
        left_interval = [self.interval[0], mid_point]
        right_interval = [mid_point, self.interval[1]]
        
        # Проверяем наличие корня в каждом из подынтервалов
        left_solver = Solver(self.func, left_interval, self.target)
        right_solver = Solver(self.func, right_interval, self.target)
        
        if left_solver.is_route_here():
            self.interval = left_interval
            return left_solver.solve()
        elif right_solver.is_route_here():
            self.interval = right_interval
            return right_solver.solve()
        else:
            raise ValueError("Корень не найден в данном интервале.")



            
    def __str__(self):
        return f"f: {self.func}\n f': {self.derivative1}\n f'': {self.derivative2}\n interval: {self.interval}\n target: {self.target}"