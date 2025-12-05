def times_in_true(names):
    true_word = "true"
    times = 0
    for letter in names:
        if letter in true_word:
            times += 1
    return times

def times_in_love(names):
    love_word = "love"
    times = 0
    for letter in names:
        if letter in love_word:
            times += 1
    return times

def calculate_love_score(name1, name2):
    in_true = times_in_true(name1 + name2)
    in_love = times_in_love(name1 + name2)
    print(f"{in_true}{in_love}")

calculate_love_score("Alberto Caballero", "Gabriela Jacuinde")

