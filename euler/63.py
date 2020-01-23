for i in range(1, 999999999+1):
    num_digits = len(str(i))
    for root in range(1, 10):
        r = round(i ** (1. / root))
        if r ** root == i:
            print(f'{r} ^ {root} = {i}')
