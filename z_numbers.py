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
