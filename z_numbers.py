import math
class z_numbers:

    def is_devideable(n: int, d: int)->bool:
        if d == 0:
            return False
        if n % d > 0:
            return False
        return True
    
    def gcd_euclid(self, a: int, b: int)->int:
        if a ==1 or b == 1:
            return a * b
        if a == 0:
            return b
        if b == 0:
            return a
        return self.gcd_euclid(self, b, a % b)
    
    def lcd(self, a: int, b: int)->int:
        return a * b / self.gcd_euclid(self, a, b)
    
    def gcd_by_products(self, a: int, b: int)->list:
        a_products = self.prime_products(self, a)
        b_products = self.prime_products(self, b)
        result = []
        a_counter = 0
        b_counter = 0
        while a_counter < len(a_products) and b_counter < len(b_products):
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


    def lcd_by_products(self, a: int, b: int)->list:
        a_products = self.prime_products(self, a)
        b_products = self.prime_products(self, b)
        result = []
        a_counter = 0
        b_counter = 0
        while a_counter < len(a_products) and b_counter < len(b_products):
            if(a_products[a_counter][0] == b_products[b_counter][0]):
                result.append([a_products[a_counter][0], max(a_products[a_counter][1], b_products[b_counter][1])])
                a_counter += 1
                b_counter += 1
                continue
            
            if(a_products[a_counter][0] < b_products[b_counter][0]):
                result.append(a_products[a_counter])
                a_counter += 1
                continue
                
            if(a_products[a_counter][0] > b_products[b_counter][0]):
                result.append(b_products[b_counter])
                b_counter += 1
                continue

        print(a_counter)
        print(b_counter)
        while a_counter < len(a_products):
            result.append(a_products[a_counter])
            a_counter += 1
            
        while b_counter < len(b_products):
            result.append(b_products[b_counter])
            b_counter += 1
        
        return result  
    
    def is_modular(self, a: int, b: int, m: int)->bool:
        return self.is_devideable(a - b, m)
    
    def is_prime(self, a: int)->bool:
        if a == 1:
            return False
        for i in range(2, int(math.sqrt(a)+1)):
            if self.is_devideable(a, i):
                return False
        return True
    
    def primes_between(self, a: int, b: int)->list:
        result = []
        for i in range(min(a, b), max(a, b)):
            if self.is_prime(self, i):
                result.append(i)
        return result
    
    def diviors(self, a: int)->list:
        result = []
        for i in range(1, a+1):
            if self.is_devideable(a, i):
                result.append(i)
        return result
    
    def prime_products(self, a: int)->list:
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
                     
    def next_prime(self, a: int)->int:
        n = a + 1
        while 1 == 1:
            if self.is_prime(self, n):
                return n
            n = n + 1
    
    def products_to_num(self, a: list)->int:
        result = 1
        for p in a:
            result *= math.pow(p[0], p[1])
        return result
    
a = z_numbers.prime_products(z_numbers,60980)
b = z_numbers.prime_products(z_numbers,14760)
print(a)
print(b)
c = z_numbers.lcd_by_products(z_numbers,14760,60980)
print(c)
print(z_numbers.products_to_num(z_numbers,c))
    

