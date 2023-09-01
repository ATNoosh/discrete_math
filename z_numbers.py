import math
class z_numbers:

    def is_devideable(n, d):
        if d == 0:
            return False
        if n % d > 0:
            return False
        return True
    
    def gcd(self, a, b):
        if a ==1 or b == 1:
            return a * b
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
    
    def prime_products(self, a):
        result = []
        p = 2
        while 1 == 1:
            print(a)
            if a == 1:
                break
            if a % p == 0:
                a = a / p
                added_before = 0
                for m in result:
                    if m[0] == p:
                        m[1] += 1
                        added_before = 1
                if added_before == 0:
                    result.append([p, 1])
            else:
                p = self.next_prime(self, p)
        return result
                     
    
    def next_prime(self, a):
        n = a + 1
        while 1 == 1:
            if self.is_prime(self, n):
                return n
            n = n + 1
    
print(z_numbers.prime_products(z_numbers,96))
    

