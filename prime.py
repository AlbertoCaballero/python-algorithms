print(list(filter(lambda x:all(x % y != 0 for y in range(2, x)), range(2, 50))))

def isPrime(a):
    if len([n for n in range(2, a) if a % n == 0]) == 1:
        return True
    return False

for x in range(2, 50):
    print(x, isPrime(x))

