import math
class z_numbers:

    def is_devideable(n, d):
        if d == 0:
            return False
        if n % d > 0:
            return False
        return True
    
    def gcd(self, a, b):
        if b == 1:
            return a
        if a == 1:
            return b
        if a == 0:
            return b
        if b == 0:
            return a
        return self.gcd(self, b, a % b)
    
    def lcd(self, a, b):
        return a * b / self.gcd(self, a, b)
    
    def is_modular(self, a, b, m):
        return self.is_devideable(a - b, m)
    
    def is_prime(self, a):
        if a == 1:
            return False
        for i in range(2, int(math.sqrt(a)+1)):
            if self.is_devideable(a, i):
                return False
        return True
    
    def primes(self, a, b):
        result = []
        for i in range(min(a, b), max(a, b)):
            if self.is_prime(self, i):
                result.append(i)
        return result
    
    def diviors(self, a):
        result = []
        for i in range(1, a+1):
            if self.is_devideable(a, i):
                result.append(i)
        return result
    
print(z_numbers.diviors(z_numbers,30))
    

