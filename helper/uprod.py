def uprod(*seqs):
    '''
    Gives all unique combinations of multiple lists that may have repeated elements
    \nhttps://stackoverflow.com/questions/19744542/itertools-product-eliminating-repeated-elements
    '''
    def inner(i):
        if i == n:
            yield tuple(result)
            return
        for elt in sets[i] - seen:
            seen.add(elt)
            result[i] = elt
            for t in inner(i+1):
                yield t
            seen.remove(elt)

    sets = [set(seq) for seq in seqs]
    n = len(sets)
    seen = set()
    result = [None] * n
    for t in inner(0):
        yield t
