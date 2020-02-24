import throw_gevent_at_it
import moon
import itertools

output_set = set()

for i in range(128):
    search_iter = itertools.permutations(moon.search_space, i)

    for permu in search_iter:
        result = throw_gevent_at_it.is_content(permu)

        if result[0]:
            output_set.add(result[1])