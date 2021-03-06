import time
from contextlib import contextmanager
import itertools
from string import printable
from typing import List

from texttable import Texttable


def preprocess(texts):
    return [[''.join(filter(lambda x: x in printable, w)) for w in t] for t in texts]


sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)



@contextmanager
def timeit_context(name, quiet= False):
    if not quiet:
        startTime = time.time()
        yield
        elapsedTime = time.time() - startTime
        print('[{}] finished in {} ms'.format(name, int(elapsedTime * 1000)))
    else:
        yield

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

def triplewise(iterable):
    "Return overlapping triplets from an iterable"
    # triplewise('ABCDEFG') -> ABC BCD CDE DEF EFG
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c

def find_indices(list_to_check, item_to_find):
    return [idx for idx, value in enumerate(list_to_check) if value == item_to_find]

def alignment_table(alignment, a, b, info_a=None, info_b=None):
    table = Texttable()
    table.set_deco(Texttable.HEADER)
    table.set_cols_align(["c", "r", "l", "r", "l"] + (['r'] if info_a else [])+ (['l'] if info_b else []))
    table.add_rows(
        [
            ['i', 'w1', 'w2', 'i', 'j']   + (['info_a'] if info_a else [])+ (['info_b'] if info_b else [])
        ] + [
            [ii, a[i] if i or i == 0 else "	      ∅-1 ", b[j] if j or j == 0 else " 	∅-2  ", i, j
             ]  + ([info_a(i) if i else "None"] if info_a else [])+ ([info_b(j) if j else None] if info_b else [])
            for ii, (i, j)
            in enumerate(alignment)]
    )
    return table.draw()


def str_in_list_at(sl: List[str], pos: int, pos_str_start: int = 0, pos_str_end: int = 0, span: int = 4) -> str:
    """
    From a list of strings return the string before or after, given the positions


    >>> str_in_list_at("abc def gef hij".split(), 0, span = 3)
    'abc'


    >>> str_in_list_at("abc def gef hij".split(), 1, pos_str_end = 2, span = 6)
    'gefhij'


    >>> str_in_list_at("abc def gef hij".split(), 2, pos_str_start = 2, span = -6)
    'cdefge'


    >>> str_in_list_at("abc def gef hij".split(), 1, pos_str_start = 2, span = 6)
    'fgefhi'

    >>> str_in_list_at("abc def gef hij".split(), 2, pos_str_end = 2, span = -6)
    'defgef'


    >>> str_in_list_at("abc def gef hij".split(), 2, span = -3)
    'def'

    >>> str_in_list_at("abc def gef hij".split(), 0, span = -3)
    ''


    >>> str_in_list_at("abc def gef hij".split(), 3, span = 3)
    'hij'


    >>> str_in_list_at("abc def gef hij".split(), 2, span = 3)
    'gef'

    >>> str_in_list_at("abc def gef hij".split(), 1, span = 6)
    'defgef'




    if the requested range is shorter, the result is also shorter as with the "abc"[:10] syntax, that
    gives "abc"


    """
    fb = sign(span)
    if fb == 0:
        return ""

    if pos_str_start == 0 and pos_str_end == 0:
        r = ""
    if pos_str_start > 0:
        r = (sl[pos][:pos_str_start] if fb < 0 else sl[pos][pos_str_start:])
    if pos_str_end > 0:
        r = (sl[pos][:pos_str_end + 1] if fb < 0 else sl[pos][pos_str_end + 1:])

    pos_new = pos + ((1 if pos_str_end or pos_str_start else 0) if fb > 0 else -1)
    span_len = abs(span)

    while True:
        if pos_new < 0 or pos_new >= len(sl):
            return r

        if fb > 0:
            r = r + sl[pos_new][:span]

            if len(r) >= span_len:
                return r[:span]
            else:
                pos_new += 1

        elif fb < 0:
            r = sl[pos_new][span:] + r

            if len(r) >= span_len:
                return r[span:]
            else:
                pos_new -= 1


def find_pos_at(seq: List[str], c_pos) -> str:
    """
    From a list of strings return the string before or after, given the positions


    >>> find_pos_at("abc def gef hij".split(), 3)
    (1, 0)
    """


    i = 0
    for iw, w in enumerate(seq):
        for ic,c in enumerate(w):
            if i == c_pos:
                return iw, ic
            i += 1

    if i == c_pos:
        return iw, ic

    return -1, -1


if __name__ == "__main__":
    import doctest

    doctest.NORMALIZE_WHITESPACE = True
    doctest.testmod()



