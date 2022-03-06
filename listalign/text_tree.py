import copy
import itertools
import pprint
from collections import defaultdict, deque

from dataclasses import dataclass
from typing import List

from listalign.helpers import timeit_context


t = "1231232bhdbkfjksdfsdjfsdjfhsdljbavfbdjvbdfjvndfjlnvljfbvjdsfbvldfshvdflkghj3z384gz8340gnrjvf vjefnvkjqerhfou34hf34hfljerbnjeqr"

s = {l: {} for l in t}

for i, l in enumerate(t[:-1]):
    s[l].update({t[i+1]: s[t[i+1]]})

class defaultlist(list):
    def __init__(self, fx):
        self._fx = fx
    def _fill(self, index):
        while len(self) <= index:
            self.append(self._fx())
    def __setitem__(self, index, value):
        self._fill(index)
        list.__setitem__(self, index, value)
    def __getitem__(self, index):
        self._fill(index)
        return list.__getitem__(self, index)

@dataclass
class Locator:
    index: int
    char: str
    following_char: str
    index_comp: int
    char_comp: List[chr]
    substract: List[int]
    difference: List[int]


def build_suffix_tree(text):
    tree = defaultdict(lambda: defaultdict(lambda: list()))

    for char_index, letter in enumerate(text):
        following_char = text[char_index + 1] if char_index + 1 < len(text) else None
        tree[letter][following_char].append(
            Locator(
                index=char_index,
                char=letter,
                following_char = following_char,
                substract=None,
                difference=None,
                index_comp=[],
                char_comp=[]
            )
        )

    return tree


def substract(tree, needle):
    for char_index, letter in enumerate(needle):
        following_char = needle[char_index + 1] if char_index + 1 < len(needle) else None
        for locator in tree[letter][following_char]:
            if not locator.substract:
                locator.substract = []
            locator.substract.append(locator.index - char_index)
            locator.char_comp.append(letter)
            locator.index_comp.append(char_index)




def traverse(tree, hay):
    sequence = []
    tree = copy.deepcopy(tree)
    for char_index, char in enumerate(hay):
        following_char = hay[char_index + 1] if char_index + 1 < len(hay) else None
        item = tree[char][following_char].pop(0)
        sequence.append(item)

    return sequence



def longest_seq(A, target):
    """ input list of elements, and target element, return longest sequence of target """
    cnt, max_val = 0, 0 # running count, and max count
    for e in A:
        cnt = cnt + 1 if e == target else 0  # add to or reset running count
        max_val = max(cnt, max_val) # update max count
    return max_val

def difference(sequence, len_needle):
    difference_sequence = []

    for sequence_index, locator in enumerate(sequence):
        if locator.substract:
            following_match = next(
                (sequence[i]
                 for i in range(sequence_index + 1, len(sequence))
                 if
                 sequence[i].substract
                 ), None)

            if following_match and following_match.substract and locator.substract:
                locator.difference = [[abs(abs(i) - abs(j))

                                       for i in locator.substract] for j in following_match.substract]

                difference_sequence.append(locator)

    return difference_sequence


def search_in_tree(hay, needle):
    hay_text = "".join("".join(word) for word in hay)
    tree = build_suffix_tree(hay_text)
    substract(tree, needle)
    chain = traverse(tree, hay_text)
    difference(chain, len(needle))
    matching_indices = find_matching_sequence_options(chain)

    matches = []
    for i, c in enumerate(needle):
        matched_occurrences = [
                match for match in matching_indices
                if i in match.index_comp
            ]
        if matched_occurrences:
            matches.append(matched_occurrences)

    matching_options = (list(itertools.zip_longest(*matches, fillvalue ='_' )))

    def sort_by_match_index(e, prev, next):
        if not isinstance(e, Locator):
            return 99999999999
        prev_index = min(prev, key=lambda x: x.index-e.index if isinstance(x, Locator) else 999999999).index

        next_index = min(next, key=lambda x: x.index-e.index if isinstance(x, Locator) else 999999999).index


        distance = abs(e.index - prev_index) + abs(e.index-next_index)
        return distance

    matching_options = [
        list(
            sorted(
                l,
                key=
                    lambda e:
                        sort_by_match_index(
                            e,
                            matching_options[i-1] if i-1 > 0 else ".",
                            matching_options[i+1]  if i <= len(matching_options) else "."
                        )
            )
        ) for i, l in enumerate(matching_options)
    ]
    score = [
        sum(
            sum( *[ll for ll in l.difference])
            for l in option
            if isinstance(l, Locator) and l.difference)
        for option in matching_options
    ]

    final_match = min(zip(score, matching_options), key=lambda sm: abs(sm[0]))

    return final_match


def find_matching_sequence_options(chain):
    return [
        locator for i, locator in enumerate(chain)
        if
        locator.substract
        or (i > 2 and
            any(dl.substract for dl in chain[i - 1:i])
            )
    ]


t = """Wie reagieren Regierungen auf das Syndrom?
Regierungsvertreter und Regierungsvertreterinnen sprechen offiziell meist von «abnormalen Gesundheitsvorfällen». Die Angelegenheit hat sich in den USA mittlerweile zur Polit-Affäre ausgeweitet. Der Leiter der CIA-Station in Wien verlor wegen seiner Untätigkeit in einem Fall sogar den Job. In den USA sind nun ein hoher CIA-Agent und eine Taskforce am Werk, die das Syndrom untersuchen sollen. Kolumbiens Präsident Iván Duque äusserte sich bei einem Besuch in New York zum Syndrom wie folgt: «Natürlich haben wir Kenntnis von dieser Situation, aber ich möchte sie den US-Behörden überlassen, die ihre eigenen Ermittlungen durchführen, weil es um ihr eigenes Personal geht.»

Was sagen die Betroffenen zum Syndrom?
Öffentliche Aussagen von Betroffenen zum Syndrom gibt es nur wenige. Das Magazin GQ sprach mit einem CIA-Mitarbeiter in Moskau, der 2017 an Symptomen litt. Er habe aufgrund seiner Übelkeit zuerst gedacht, dass er sich eine Lebensmittelvergiftung eingefangen hätte. Beim Versuch, ins Bad zu gehen, sei er mehrmals umgefallen, da er starken Schwindel verspürte. Es habe sich angefühlt, als ob er sich übergeben müsse und gleichzeitig in Ohnmacht falle. Ein weiteres Problem sei gewesen, dass er «keinen Ton» mehr gehört habe.

"""

with timeit_context("tree match"):
    search_in_tree([t.split()], "Öffentliche Aussagen von Betroffenen zum Syndrom gibt es nur wenige".replace(" ", ""))


    pprint.pprint(search_in_tree([t.split()], "Öffentliche Aussagen von Betroffenen zum Syndrom gibt es nur wenige".replace(" ", "")))


def find_following_zero_texts(texts, w_pos_b):
    for iz, t in enumerate(texts[1][w_pos_b + 1:w_pos_b + 10]):
        if t != "":
            return iz + 1

    return 1


if __name__ == "__main__":
    import time
    import paired
    import matplotlib.pyplot as plt

    with open("../test/data/faust.txt") as f:
        text = "".join(f.readlines())[:100000000].replace("", "")

    words_a = text.replace("n", "n ").split(" ")
    words_b = text.replace("m", "m ").split(" ")

    print("does not work for shifts")
    seq_1 = 'cere frangit brum'.split(' ')
    seq_2 = 'frangit cerebrum'.split(' ')

    """
    print(alignment_table(suffix_align(seq_1, seq_2), seq_1, seq_2))

    a = ['jumpedo', 'verthelazydo', 'gThequickbro', 'wnfo', 'x']
    b = ['jumpe', 'd', 'ove', 'r', 'the', '', 'lazy', 'dog', 'The', '', 'quick', 'brown', 'fox', '']
    print(alignment_table(suffix_align(a, b), a, b))
    a = ['jumpedo', 'verthelazydo', 'gThequickbro', 'wnfo', 'x']
    b = ['jump', 'd', 'ove', 'r', 'the', '', 'lazy', 'dog', 'The', '', 'quick', 'brown', 'fox', '']
    print(alignment_table(suffix_align(b, a), b, a))

    seq_1 = 'Thequickbrownfoxjumpedoverthelazydog'.replace('o', 'o ').split(' ')
    seq_2 = 'The quick brown fox jumped over the lazy dog'.replace('e', 'e ').split(' ')

    print(alignment_table(suffix_align(seq_1, seq_2), seq_1, seq_2))

    print(alignment_table(paired.align(seq_1, seq_2), seq_1, seq_2))

    with timeit_context('suffix-align-1000-1000'):
        path = (suffix_align(words_a[:1000], words_b[:1000]))
        print(alignment_table(path, words_a, words_b))

    with timeit_context('paired-1000-1000'):
        print(paired.align(words_a[:1000], words_b[:1000]))

    with timeit_context(f'full suffix-align on {len(words_a)}x{len(words_b)}'):
        x = suffix_align(words_a, words_b)


    def perf_plot():
        res = {}
        for i in range(100, 1000, 10):
            start_time = time.time()
            suffix_align(words_a[:i], words_b[:i])
            res[i] = time.time() - start_time
            print(f'{i}.', end='')

        plt.plot(list(res.keys()), list(res.values()))
        plt.xlabel('length of lists', fontsize=18)
        plt.ylabel('s per run', fontsize=16)
        fig1 = plt.gcf()
        plt.show()
        plt.draw()
        fig1.savefig('../../suffix-align.png', dpi=100)


    with timeit_context('performance plot'):
        perf_plot()


    def perf_plot_paired():
        res = {}
        for i in range(50, 500, 10):
            start_time = time.time()
            suffix_align(words_a[:i], words_b[:i])
            la = time.time() - start_time
            start_time = time.time()
            paired.align(words_a[:i], words_b[:i])
            pa = time.time() - start_time
            res[i] = (la, pa)
            print(f'{i}.', end='')

        plt.plot(list(res.keys()), list(x1[0] for x1 in res.values()), label='list align')
        plt.plot(list(res.keys()), list(x2[1] for x2 in res.values()), label='paired align')

        plt.xlabel('length of lists', fontsize=18)
        plt.ylabel('s per run', fontsize=16)
        plt.legend()
        fig1 = plt.gcf()
        plt.show()
        plt.draw()
        fig1.savefig('../../suffix-align_pa.png', dpi=100)


    with timeit_context('performance plot against paired'):
        perf_plot_paired()

    import doctest

    doctest.NORMALIZE_WHITESPACE = True
    doctest.testmod()
    
    """
