import random
from collections import Counter
from pprint import pprint
import regex as regex
from listalign.helpers import timeit_context, alignment_table, triplewise
import parasail


def word_string_dict(list_words):
    string = "".join(list_words).encode("ascii",  errors="replace")
    index_mapping = {}
    i = 0
    for n, w in enumerate(list_words):
        for c in w:
            index_mapping[i] = n
            i += 1

    return string, index_mapping


cigar_op_format = {
    "=": lambda i, pos1, pos2: (range(pos1, pos1 + i), range(pos2, pos2 + i), pos1 + i, pos2 + i),
    "M": lambda i, pos1, pos2: (range(pos1, pos1 + i), range(pos2, pos2 + i), pos1 + i, pos2 + i),
    "D": lambda i, pos1, pos2: ([None] * (i), range(pos2, pos2 + i), pos1, pos2 + i),
    "I": lambda i, pos1, pos2: (range(pos1, pos1 + i), [None] * (i), pos1 + i, pos2),
    "S": lambda i, pos1, pos2: ([None] * (i), [None] * (i), pos1, pos2 + i),
    "X": lambda i, pos1, pos2: ([None] * (i), [None] * (i), pos1 + i, pos2 + i),
}


def cigar_to_table(pos1, pos2, cigar_str, str_a, str_b):
    str_a = str_a.decode().lower()
    str_b = str_b.decode().lower()
    table = []
    for i_op in regex.findall('\d+[A-Z=]', cigar_str):
        i, op = regex.match('(\d+)([A-Z=])', i_op).groups()
        i = int(i)

        ms, ns, pos1, pos2 = cigar_op_format[op](i, pos1, pos2)
        for m, n in zip(ms, ns):
            if m and n:
                try:
                    # print (f"{m=}-{str_a[m]=}<->{n=}-{str_b[n]=} {cigar_str}")
                    assert str_a[m] == str_b[n]
                except Exception as e:
                    raise
            table.append((m, n,))

    return table


def align(list_a, list_b):
    str_a, m_a = word_string_dict(list_a)
    str_b, m_b = word_string_dict(list_b)
    extra = {}

    with timeit_context("swalign", quiet=True):
        pass
        # result = sw.align(str_a,str_b)
        # alignment = cigar_to_table(result.r_pos, result.cigar_str, str_a, str_b)
        # result.dump()

    with timeit_context("parasail", quiet=True):
        result = parasail.sw_trace_scan_16(str_a, str_b, 100, 0, parasail.blosum62)

        alignment = cigar_to_table(result.cigar.beg_query, result.cigar.beg_ref, result.cigar.decode.decode("utf8"),
                                   str_a, str_b)

    extra["cigar"] = result.cigar.decode.decode("utf8")

    raw_alignment = []
    for a, b in (alignment):
        raw_alignment.append((m_a[a] if a in m_a else None, m_b[b] if b != None else None))
    prev_result = list(sorted(set(
        raw_alignment
    ), key=lambda x: (x[0] if x[0] else 0) + (x[1] if x[1] else 1) / len(list_b)))

    nones = [e for e in prev_result if e[1] == None]
    for n in nones:
        if any(n[0] == e[0] and e[0] != None for e in prev_result):
            prev_result.pop(prev_result.index(n))



    too_splitted = [b for a,b,c in triplewise(prev_result) if (a[0] and b[1] and (list_b[b[1]] in list_a[a[0]] )) or (a[0] and b[1] and (list_b[b[1]] in list_a[c[0]]))]
    #too_splitted = []
    prev_result = [e for e in prev_result if e not in too_splitted]

    too_far_neighbors = [b for a,b,c in triplewise(prev_result) if (b[0] - a[0] > 3 if a[0] and b[0] else True) and (c[0] - b[0] > 3 if b[0] and c[0] else True)]
    #prev_result = [e for e in prev_result if e not in too_far_neighbors]

    return prev_result, extra


def stuff_socks(prev_result, window, l_a, l_b):
    items = list(sorted(prev_result.items(), key=lambda x: x[0] if x[0] else -1))
    for i, (i_a, i_b) in enumerate(items):
        if i_b == None:
            next_not_None_forwards = next((e for e in items[i:i + window] if e[1] != None), None)
            next_not_None_backwards = next((e for e in items[i:i - window: -1] if e[1] != None), None)

            if next_not_None_forwards and next_not_None_backwards \
                    and next_not_None_forwards[1] > next_not_None_backwards[1]:
                for ai, aw in enumerate(l_a[next_not_None_backwards[0]: next_not_None_forwards[0]]):
                    b_i_w = max(
                        enumerate(l_b[next_not_None_backwards[1]: next_not_None_forwards[1]]),
                        key=lambda x: jellyfish.jaro_similarity(x[1], aw)
                    )

                    prev_result[next_not_None_backwards[0] + ai] = b_i_w[0] + next_not_None_backwards[1] - 4


if __name__ == "__main__":
    from faker import Faker
    import pandas
    import matplotlib.pyplot as plt
    import rapidfuzz

    scores = []
    for i_exeperiment in range(300):

        text_a = ""
        text_b = ""
        fake = Faker()

        for _ in range(50):

            t = fake.text()
            if random.random() > 0.1:
                text_a += t
                if random.random() > 0.3:
                    text_b += t

        for _ in range(10):

            t = fake.text()
            if random.random() > 0.5:
                text_a = text_a + t
            else:
                text_a = t + text_a

        text_b = text_b.replace("e", "_")
        text_a = text_a.replace("o", "?")

        with timeit_context("match", quiet=True):
            text_b = text_b.replace("u", "a")
            l_a = text_a.split()
            for i, aw in enumerate(l_a):
                if random.random() > 0.5 and i + 1 < len(l_a):
                    l_a[i] = l_a[i] + l_a[i + 1]
                    l_a[i + 1] = ""

            l_b = text_b.split()
            word_to_word_alignment, extra = align(l_a, l_b)

        ata = "".join(l_a[a] for a, b in word_to_word_alignment if a)
        bta = "".join(l_b[b] for a, b in word_to_word_alignment if a)
        score = rapidfuzz.string_metric.normalized_levenshtein(ata, bta)
        ground_similarity = rapidfuzz.string_metric.normalized_levenshtein(text_a, text_b)
        word_align_score = \
            sum([
                rapidfuzz.string_metric.jaro_similarity(l_a[a], l_b[b])
                for a, b in word_to_word_alignment if a
            ]) / len([x for x in word_to_word_alignment if x])

        C = Counter([c for c in extra["cigar"] if c not in "1234567890"])
        letter_prob = {
            c: n / len(extra["cigar"]) * 100 for c, n in C.items()
        }
        d = {
            "~ align(a, b) ": score,
            "a ~ b": ground_similarity,
            "corrupted": int(word_align_score < ground_similarity) * 100,
            "word_align_score": word_align_score,
            # **letter_prob,
            # "i corrupting": int("I" in extra["cigar"] and word_align_score < 40) * 100,
            # "d corrupting": int("D" in extra["cigar"] and word_align_score < 40) * 100,
            # "x corrupting": int("X" in extra["cigar"] and word_align_score < 40) * 100,
            # "= corrupting": int("=" in extra["cigar"] and word_align_score < 40) * 100,
            "cigar": extra["cigar"]
        }
        scores.append(d)

        pprint(d)

        print(len(l_a))
        if (int(word_align_score < ground_similarity)):
            if word_align_score < 50:
                with open("a.fasta", "w+") as f:
                    f.write(f">a vs b - {i_exeperiment}\n")
                    f.write(text_a.replace("/n", "").replace(" ", ""))
                    f.write("*\n")
                with open("b.fasta", "w+") as f:
                    f.write(f">a vs b - {i_exeperiment}\n")
                    f.write(text_b.replace("/n", "").replace(" ", ""))
                    f.write("*\n")

            print(alignment_table(word_to_word_alignment, l_a, l_b))

    df = pandas.DataFrame(scores)

    fig, ax = plt.subplots(figsize=(6, 4))
    df.plot(kind="hist",
            # stacked=True,
            alpha=0.7,
            bins=30)
    plt.show()
