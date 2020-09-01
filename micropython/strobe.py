def light_gen():

    r, g, b = (0, 0), (255, -1), (0, 1)

    while True:
        r = (r[0] + r[1], r[1])
        g = (g[0] + g[1], g[1])
        b = (b[0] + b[1], b[1])

        for item in [r, g, b]:
            if item[0] == 0 or item[0] == 255:
                if item[1] == -1:
                    item = (item[0], 0)
                elif item[1] == 0:
                    item = (item[0], 1)
                elif item[1] == 1:
                    item = (item[0], -1)
                else:
                    raise HolUpException

        yield (r[0], g[0], b[0])


tester = light_gen()

for _ in range(250):
    print(next(tester))

for _ in range(100):
    print(next(tester))
