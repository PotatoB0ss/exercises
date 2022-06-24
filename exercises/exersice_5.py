from functools import reduce


def count_find_num(primesL, limit):
    secondary = reduce(lambda x, y: x * y, primesL)
    result = [secondary] + [i * secondary for i in primesL]
    for _ in range(15):
        result.extend([i * j for i in result for j in primesL])
        result = filter(lambda x: x <= limit, result)
        result = list(set(result))

    return [] if not result else [len(result), max(result)]


