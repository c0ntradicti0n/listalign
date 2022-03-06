import random
from pprint import pprint

import jellyfish as jellyfish
import regex as regex
jellyfish.jaro_distance(u'jellyfish', u'smellyfish')
from listalign.helpers import timeit_context, alignment_table
import parasail


def word_string_dict(list_words):
    string = " ".join(list_words).encode("ascii", errors="ignore")
    index_mapping = {}
    i = 0
    for n, w in enumerate(list_words):
        for c in w:
           index_mapping[i] = n
           i += 1
        index_mapping[i] = n
        i += 1
    return string, index_mapping



cigar_op_format = {
    "=": lambda i, pos1, pos2: (range(pos1, pos1+i), range(pos2, pos2+i), pos1 + i, pos2 + i),
    "D": lambda i, pos1, pos2: ([None]*(i), range(pos2, pos2+i), pos1, pos2 + i),
    "I": lambda i, pos1, pos2: (range(pos1, pos1+i), [None] * (i), pos1 + i, pos2),
    "S": lambda i, pos1, pos2: ([None]*(i), [None]*(i), pos1, pos2 + i),
    "X": lambda i, pos1, pos2: (range(pos1, pos1+i), range(pos2, pos2+i), pos1 + i, pos2 + i),
}

def cigar_to_table(pos1, cigar_str, str_a, str_b):
    table = []
    pos2 = 0
    for i_op in regex.findall('\d+[A-Z=]', cigar_str):
        i, op = regex.match('(\d+)([A-Z=])', i_op).groups()
        i = int(i)

        ms, ns , pos1, pos2 = cigar_op_format[op](i, pos1, pos2)
        for m, n in zip(ms, ns):
            table.append((m, n,))

    return table


def align(list_a, list_b):
    str_a, m_a = word_string_dict(list_a)
    str_b, m_b = word_string_dict(list_b)

    with timeit_context("parasail"):
        result = parasail.sw_trace_scan_16(str_a, str_b, 10, 1, parasail.blosum62)
        print((result.cigar.decode.decode("utf8")))
        alignment = cigar_to_table(result.cigar.beg_ref, result.cigar.decode.decode("utf8"), str_a, str_b)
        print(t)

    prev_result = list(sorted(set(
        [(m_a[a] if a in m_a else None, m_b[b] if b != None else None) for a, b in (alignment)]
    ), key=lambda x:x[0] if x[0] else 0))

    #stuff_socks(prev_result, 3, list_a, list_b)

    return prev_result

def stuff_socks(prev_result, window, l_a, l_b):
    items = list(sorted(prev_result.items(), key=lambda x: x[0] if x[0] else -1))
    for i, (i_a, i_b) in enumerate(items):
        if i_b == None:
            next_not_None_forwards = next((e for e in items[i:i+window] if e[1] !=None), None)
            next_not_None_backwards = next((e for e in items[i:i-window: -1] if e[1] !=None), None)

            if next_not_None_forwards and next_not_None_backwards \
                    and next_not_None_forwards[1] > next_not_None_backwards[1] :
                for ai, aw in enumerate(l_a[next_not_None_backwards[0]: next_not_None_forwards[0]]):

                    b_i_w = max(
                        enumerate(l_b[next_not_None_backwards[1]: next_not_None_forwards[1]]),
                        key=lambda x: jellyfish.jaro_similarity(x[1], aw)
                    )

                    prev_result[next_not_None_backwards[0] + ai] = b_i_w[0] +next_not_None_backwards[1] -4


if __name__=="__main__":
    from faker import Faker

    text_a = "\ufb01"
    text_b = "\ufb01"
    fake = Faker()
    for _ in range(100):

        t = fake.text()
        if random.random() > 0.1:
            text_a += t
            if random.random() > 0.3:
                text_b += t

    text_b = text_b.replace("e", "_")
    text_a = text_a.replace("o", "?")

    with timeit_context("match"):
        #text_b = text_b.replace("e", "a")
        l_a = text_a.split()
        for i, aw in enumerate(l_a):
            if random.random()>0.5 and i+1 < len(l_a):
                l_a[i] = l_a[i] + l_a[i+1]
                l_a[i+1] = ""



        l_b = text_b.split()
        word_to_word_alignment = align(l_a,l_b)
        pprint(word_to_word_alignment)

        print(alignment_table(word_to_word_alignment, l_a, l_b))

    print(len(l_a))
