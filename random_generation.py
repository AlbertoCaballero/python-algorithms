import random

random_integer = random.randint(1, 10)
print(random_integer)

random_floating = random.random()
print(random_floating)

random_uniform = random.uniform(1, 10)
print(random_uniform)

def coin_toss ():
    print("HEADS") if random.randint(0, 1) == 0 else print("TAILS")

coin_toss()

hobbies = ["Coding", "Mechanics", "Algorithms", "Running", "Building"]
print(random.choice(hobbies))

