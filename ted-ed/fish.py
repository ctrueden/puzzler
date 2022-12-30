# https://www.youtube.com/watch?v=lLOALyWls2k

a_tanks = 4; a_sharks = 2
b_tanks = 2; b_sharks = 4

max_tanks = 13
creature_total = 50

for c_tanks in range(0, max_tanks + 1):
    # We know the total number of tanks must be 13 or less.
    if a_tanks + b_tanks + c_tanks > max_tanks:
        # Total number of tanks is too many; skip this one.
        continue

    # We know there must be at least 1 fish per tank, and no more than 50 fish per tank. ;-)
    for fish_per_tank in range(1, creature_total):
        a_fishes = a_tanks*fish_per_tank
        b_fishes = b_tanks*fish_per_tank
        c_fishes = c_tanks*fish_per_tank
        fish_total = a_fishes + b_fishes + c_fishes

        # We know there can be between 1 and 7 sharks in C zone.
        for c_sharks in range(1, 8):
            shark_total = a_sharks + b_sharks + c_sharks
            if c_sharks == a_sharks or c_sharks == b_sharks:
                # No two sectors have the same number of sharks; skip this one.
                continue

            if fish_total + shark_total != creature_total:
                # The number of fish and sharks does not match the known total of 50; skip this one.
                continue

            # Everything works! This is an answer.
            print(f"c_tanks = {c_tanks}, fish_per_tank = {fish_per_tank}, c_sharks = {c_sharks}")
