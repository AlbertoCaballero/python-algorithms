def factorial(n):
    if n<0: 
        return 0
    elif n>1:
        return n*factorial(n-1)
    return 1

number = input('Factorial: ')
print(factorial(number))

