class z_numbers:
    def is_devideable(n, d):
        if d == 0:
            return False
        if n % d > 0:
            return False
        return True

print(z_numbers.is_devideable(100, 0))
