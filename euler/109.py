# How many ways to reach a winnable score [2, 4, 6, 8, ..., 40, 25, 50] from score with 0, 1 or 2 darts?

winnable = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 25, 26, 28, 30, 32, 34, 36, 38, 40, 50)

def ways(score):
    ways = 0
    for left in winnable:
        ways += ways0(score, left) + ways1(score, left) + ways2(score, left)
    return ways

# How many ways to reach the target if you have no throws left?
def ways0(score, target):
    if score == target: print(f'[0 -> {target}] {score}')
    return 1 if score == target else 0

# How many ways to reach the target if you have one throw left?
def ways1(score, target):
    needed = score - target
    if needed <= 0: return 0
    ways = 0
    if (needed >= 1 and needed <= 20) or needed == 25:
        print(f'[1 -> {target}] S{needed}')
        ways += 1 # singles
    if needed % 2 == 0 and (needed <= 40 or needed == 50):
        print(f'[1 -> {target}] D{needed // 2}')
        ways += 1 # doubles
    return ways

# How many ways to reach the target if you have two throws left?
def ways2(score, target):
    ways = 0
    for mid in range(1, target // 2 + 1):
        print(f'[2 -> {target}] {ways1(score, target + mid)} + {ways1(score - mid, target)}')
        ways += ways1(score, target + mid) + ways1(score - mid, target)
    print(f'[2] ways2({score}, {target}) => {ways}')
    return ways

print(ways(6))
