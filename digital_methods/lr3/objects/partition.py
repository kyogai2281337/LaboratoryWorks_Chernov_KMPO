def nilLamb(const, val):
    return const

class Partition:
    def __init__(self, lamb, pow, polarity=1, const=1):
        self.const = const
        self.lamb = lamb
        self.polarity = polarity # 1 or -1
        self.pow = pow
    
    def solve(self, val):
        return (self.lamb(self.const, val)*self.polarity)**self.pow
    
    def derivative(self):
        if self.pow == 1:
            return Partition(nilLamb, self.pow-1, self.polarity, self.const)
        elif self.pow == 0:
            return 0
        else:
            return Partition(self.lamb, self.pow-1, self.polarity, self.const*self.pow)
        
    def inderivative(self):
        """Return the integral of this Partition"""
        if self.pow == 1:
            return Partition(lamb=self.lamb, pow=self.pow+1, polarity=self.polarity, const=self.const)
        elif self.pow == 0:
            return Partition(lamb=lambda const, val: const*val, pow=self.pow+1, polarity=self.polarity, const=self.const)
        else:
            return Partition(lamb=lambda const, val: self.lamb(const, val), pow=self.pow+1, polarity=self.polarity, const=self.const*self.pow)
        
    def __str__(self) -> str:
        if self.pow == 0:
            return f"{'+' if self.polarity == 1 else '-'}{abs(self.const)}"
        elif self.pow == 1:
            if abs(self.const) == 1:
                return f"{'+' if self.polarity == 1 else '-'}x"
            else:
                return f"{'+' if self.polarity == 1 else '-'}{abs(self.const)}x"
        else:
            if abs(self.const) == 1:
                return f"{'+' if self.polarity == 1 else '-'}x^{self.pow}"
            else:
                return f"{'+' if self.polarity == 1 else '-'}{abs(self.const)}x^{self.pow}"

