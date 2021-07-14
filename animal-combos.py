# A = number of animals
# total pairs = A!
# pairs with matching animal = ???
# pairs are there with two flipped animals =

animals = ['cow', 'duck', 'horse', 'pig', 'sheep', 'monkey', 'turkey', 'pigeon', 'weasel', 'hamster', 'rabbit', 'cat', 'dog', 'fish']

def print_combo(butts):
    print('  ' + ', '.join([f'{animals[i]}-{animals[butts[i]]}' for i in range(len(butts))]))

def correct(butts):
    for i in range(len(butts)):
        # head = i, butt = butts[i]
        head = i
        butt = butts[i]
        if butt is None: return True
        for j in range(i):
            if butts[j] == butt: return False # cannot reuse a butt!
        if head == butt: return False # head and butt match. Bad!
        if butts[butt] == i: return False # swapped head-butt pair. Bad!
    return True

def combos(butts, index=0):
    if index == len(butts):
        if correct(butts):
            #print_combo(butts)
            return 1
        return 0
    total = 0
    new_butts = butts[:]
    for i in range(len(butts)):
        new_butts[index] = i
        if not correct(new_butts):
            continue
        total += combos(new_butts, index + 1)
    return total

for c in range(3, len(animals)):
    some_animals = animals[:c]
    print(some_animals)
    print(f'{c} animals => {combos([None] * len(some_animals))}')


