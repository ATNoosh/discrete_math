import math
class z_numbers:

    def is_devideable(n, d):
        if d == 0:
            return False
        if n % d > 0:
            return False
        return True
    
    def gcd_euclid(self, a, b):
        if a ==1 or b == 1:
            return a * b
        if a == 0:
            return b
        if b == 0:
            return a
        return self.gcd_euclid(self, b, a % b)
    
    def lcd(self, a, b):
        return a * b / self.gcd_euclid(self, a, b)
    
    def gcd_by_products(self, a, b):
        a_products = self.prime_products(self, a)
        b_products = self.prime_products(self, b)
        result = []
        
        a_counter = 0
        b_counter = 0
        while a_counter < len(a_products) and b_counter < len(b_products):
            print(a_counter)
            print(b_counter)
            if(a_products[a_counter][0] == b_products[b_counter][0]):
                result.append([a_products[a_counter][0], min(a_products[a_counter][1], b_products[b_counter][1])])
                a_counter += 1
                b_counter += 1
                continue
            
            if(a_products[a_counter][0] < b_products[b_counter][0]):
                a_counter += 1
                continue
                
            if(a_products[a_counter][0] > b_products[b_counter][0]):
                b_counter += 1
                continue
        
        return result
            
    
    def is_modular(self, a, b, m):
        return self.is_devideable(a - b, m)
    
    def is_prime(self, a):
        if a == 1:
            return False
        for i in range(2, int(math.sqrt(a)+1)):
            if self.is_devideable(a, i):
                return False
        return True
    
    def primes_between(self, a, b):
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
a = z_numbers.prime_products(z_numbers,600)
b = z_numbers.prime_products(z_numbers,180)
print(a)
print(b)
print(z_numbers.gcd_by_products(z_numbers,180,600))
    

