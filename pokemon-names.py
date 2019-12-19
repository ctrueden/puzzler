from random import randrange
def covered(names_per_person):
    successes = 0
    iterations = 10000
    num_people = 150
    num_pokemon = 200
    for i in range(iterations):
        counts = [0 for x in range(num_pokemon)]
        for person in range(num_people):
            for name in range(names_per_person):
                chosen = randrange(0, num_pokemon)
                counts[chosen] = 1
        if sum(counts) == num_pokemon:
            successes += 1

    print(f'if {num_people} people say {names_per_person} each, they cover all {num_pokemon} pokemon {100*successes/iterations}% of the time')

for i in range(12, 15):
    covered(i)
