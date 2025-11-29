print("MAMA MIA PIZZERIAAAAAA!")

size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("You want pepperoni? Y or N: ")
extra_chesse = input("You want extra chesse? Y or N: ")

total_cost = 0

# Pizz size
if size == "S":
    total_cost += 15
elif size == "M":
    total_cost += 20
elif size == "L":
    total_cost += 25

# Pepperoni
if pepperoni == "Y":
    if size == "S":
        total_cost += 2
    else:
        total_cost += 3

# extra chesse
if extra_chesse == "Y":
    total_cost += 1

print(f"Total: ${total_cost}")

