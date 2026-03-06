import sys

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

iterations = 15
if len(sys.argv) > 1:
    iterations = sys.argv[1]

for i in range(0, int(iterations), 1):
    print(f"{i}: {fibonacci(i)}" )
