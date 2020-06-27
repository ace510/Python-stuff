import itertools
import moon

for i in range(10):
    tater = itertools.combinations_with_replacement(moon.search_space, i)
    langy = 0
    for j in tater:
        langy += 1

    print(f'a string of {i} length has {langy} possibilites')