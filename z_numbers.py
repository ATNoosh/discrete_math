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

print(z_numbers.is_devideable(100, 0))
print(z_numbers.gcd(z_numbers,18888,124444))
