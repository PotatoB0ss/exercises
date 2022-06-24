import itertools


def bananas(s) -> set:
    word = 'banana'
    result = set()
    for comb in list(itertools.combinations(range(len(s)), len(s) - len(word))):
        arr = list(s)

        for n in comb:
            arr[n] = '-'

        if ''.join(arr).replace('-', '') == word:
            result.add(''.join(arr))

    return result


