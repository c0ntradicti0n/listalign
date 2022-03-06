from dataclasses import dataclass, field
import itertools
from Levenshtein import jaro

from listalign.helpers import timeit_context
import visualize



@dataclass(unsafe_hash=True)
class Locator:
    char: str
    index: list = field(default_factory=list, compare=False)

    def __str__(self):
        return self.char

    def __repr__(self):
        return self.char + "["+ str(self.index) + "]"


def make_tree(string):
    tree = {Locator(char=l): {} for l in set(string)}

    for i, l in enumerate(string[:-1]):
        l_0 = findLocator(l, tree)
        l_0.index.append(i)
        l_1 = findLocator(string[i + 1], tree)
        tree[l_0].update({l_1: tree[l_1]})

    return tree


def findLocator(l, tree):
    l__0 = Locator(char=l)
    l_0 = next((k for k in tree.keys() if k == l__0), None)
    return l_0



def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def evaluate(zuege, t1, t2):
    sim = jaro(t2, "".join(l.char for l in zuege))
    S = sum([ l1.index for l1 in zuege]) + 1

    dS = sum([abs(l2.index - l1.index+1) for l1, l2 in pairwise(zuege)])
    dist = dS / S
    return sim - dist


def noMoves(zuege, t1, t2, i, tree):
    if i >= len(t2) or t2[i] == None or all(t in zuege for t in t2):
        return True
    return False


def genereateMoves_horizontal(tree, t2, i):
    char = t2[i]
    l = findLocator(char, tree)
    moves = [[Locator(char=char, index=_i)] for _i in l.index]
    return moves


def genereateMoves_vertical(tree, t2, i):
    moves = []
    char = t2[i]
    l1 = findLocator(char, tree)



    for index_l1 in l1.index:
        k = i

        _l1 = Locator(char=char, index=index_l1)
        move = []
        move.append(_l1)

        for j in range(i + 1, len(t2)):
            char_next = t2[j]
            l2 = findLocator(char_next, tree)

            if index_l1 + 1 in l2.index:
                l = Locator(char=char_next, index=index_l1 + 1)
                move.append(l)
            else:
                break

            index_l1 = index_l1 + 1

            k = j
        if move:
            _move = [s for s in move]
            moves.append(_move)

    return moves


def nearestMove(t, zug):
    return zug.i - zug.i


bestMove = {}


@visualize.visualize_recursive(do_or_not=True)
def minimax(value, horizon, depth, alpha, beta, t1, t2, zug, zuege, tree, i):
    if zug == None:
        zug = []
    if (horizon == 0 or noMoves(zuege=zug, t1=t1, t2=t2, tree=tree, i=i)):
        return evaluate(zug, t1, t2)
    maxWert = alpha # if alpha > new_value else new_value

    search_next_chars = not depth % 2 == 0
    if search_next_chars:
        Zugliste = genereateMoves_horizontal(tree, t2, i)
        Zugliste = sorted(Zugliste, key=lambda z: z[0].index - zug[-1].index if zug else 0)
    if not search_next_chars:
        Zugliste = genereateMoves_vertical(tree, t2, i)
        Zugliste = sorted(Zugliste, key=lambda m: -len(m))

    for Zug in Zugliste:
        # fuehreZugAus(tree, Zug);
        full_move = zug + Zug
        wert = -minimax(
            value=-value,
            horizon=horizon - ( 1 if search_next_chars else 0 ),
            depth=depth + 1 ,
            alpha=-beta,
            beta=-maxWert,
            t1=t1,
            t2=t2,
            zug=full_move,
            zuege=zuege,
            tree=tree,
            i=i + (len(Zug))
        )
        # macheZugRueckgaengig(Zug);
        if (wert > maxWert):
            maxWert = wert
            if horizon == 1:
                bestMove[horizon] = full_move
            if (maxWert >= beta):
                break

    return maxWert


def align(t1, t2):
    global bestMove
    bestMove = {}
    tree = make_tree(t)
    variant = minimax(
        value=-0,
        t1=t1,
        t2=t2,
        horizon=3,
        depth=0,
        alpha=-100,
        beta=100,
        tree=tree,
        zug=None,
        zuege=[],
        i=0
    )
    return bestMove


t = """Kunstvolle Loopings Beim Berliner Skater-Verbot geht es auch um die Frage, """ #wer die Deutungshoheit hat, was Kultur sein soll und wer an ihr in welcher Form teilnehmen darf. Anderswo wird die Skater-Subkultur längst von den großen Kulturinstitutionen gefeiert und zieht ein ganz eigenes Publikum an: Die Plätze vor dem Macba in Barcelona und vor der Casa da Musica in Porto haben sich zu internationalen Skater-Spots entwickelt, bei der São-Paulo-Biennale und vor Frank Gehrys neuem Kulturzentrum in Arles hat die Künstlerin Koo Jeong A fluoriszierende Halbkugeln in den Boden gesenkt, die als Halfpipe genutzt werden dürfen; bis spät in die Nacht sausen dort die Skater herum und führen vor, welche kunstvollen Loopings zwischen Skulptur und Performance möglich sind. In Berlin, wo man sich gerade das größte Playmobilschloss der Welt gebaut hat, will man mit all diesen Formen von Gegenwart nichts zu tun haben:
#"""

t2 = """Skater-Verbot Kunstvolle Loopings geht es auch um""" #wird die Form teilnehmen darf"""


def name_from_minimax_tree_args(ret, *args, **kwrags):
    try:
        value = kwrags['value']
        alpha = kwrags['alpha']
        beta = kwrags['beta']
        depth = kwrags['depth']

        if kwrags['zug']:
            chars = "".join([l.char for l in kwrags['zug']])
        else:
            chars = 'None'
        return chars + f"\n{ret=:0.2f} \n{value=:0.2f} \n{alpha=:0.2f} \n{beta=:0.2f} \n{depth=}"
    except Exception as e:
        raise


def depth_from_minimax_tree_args(*args, **kwrags):
    try:
        depth = kwrags['depth']

        return depth
    except Exception as e:
        raise


with visualize.visualize_context(
        "super_thing.png",
        node_name=name_from_minimax_tree_args,
        get_depth=depth_from_minimax_tree_args

) as v:
    with timeit_context("match"):
        res = (align(t, t2))
print(res)
