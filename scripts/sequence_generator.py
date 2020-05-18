import string
import itertools


search_space =string.ascii_lowercase

def seq_generator(search_space, maximum_length):
    for i in range(maximum_length):
        for j in itertools.combinations_with_replacement(search_space,i):
            yield j