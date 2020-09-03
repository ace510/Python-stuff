from collections import Counter
x = "ABRACADABRA"
x_counter= Counter(x)
for key, value in x_counter.items():
    print(key,value)