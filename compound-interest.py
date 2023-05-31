
def compound_interest(principal, rate, time):
    amount = principal * (pow(1 + rate / 100, time))
    comp = amount - principal
    return comp

total = compound_interest(200000, 10.25, 25)
total += 200000
print(total)
