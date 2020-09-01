from Bjorkenson import search_space, exeggutor
import random

# itertools.permutations(search_space, i )
chain_space = [i for i in search_space]
chain_space.append("Cheese")


def def_jam():
    while True:
        output_lis = []
        for i in range(72):
            letter = random.choice(chain_space)
            if letter != "Cheese":
                output_lis.append(letter)
            else:
                break
        output_str = "".join(output_lis)
        yield output_str


output = ""

teth = def_jam()

while not output:
    next_cmd = next(teth)
    output = exeggutor(next_cmd)

print(output)
