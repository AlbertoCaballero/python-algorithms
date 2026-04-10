#  print(list(filter(lambda x:all(x % y != 0 for y in range(2, x)), range(2, 50))))

def isPrime(num):
    divisors = [n for n in range(1, num) if num % n == 0]
    if len(divisors) == 1:
        return True
    return False

for x in range(2, 50):
    print(x, isPrime(x))

