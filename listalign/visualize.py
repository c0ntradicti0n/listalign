import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

G = None
_node_name = None
_get_depth = None
tree_nodes = {}
ROOT = "root"

i = 0
def visualize_recursive(do_or_not):
    global G
    global _node_name
    global tree_nodes
    global i

    def decorator(f):
        global G
        global _node_name
        global tree_nodes
        global i

        if not do_or_not:
            return f

        def f_new(*args, **kwargs):
            global G
            global _node_name
            global tree_nodes
            global i

            ret = f(*args, **kwargs)
            new_node=i
            new_node_label = _node_name(ret, *args, **kwargs)
            depth = _get_depth(*args, **kwargs)

            if depth-1 in tree_nodes:
                before_node = tree_nodes[depth-1]
            else:
                before_node = ROOT

            G.add_node(
                node_for_adding=new_node,
                **{**kwargs, "rest": args, "label": new_node_label}
            )
            G.add_edge(before_node, new_node, label = str(i))
            tree_nodes[depth] = new_node
            i += 1

            return ret
        return f_new
    return decorator


class visualize_context:
    def __init__(self,
            filename = "call_graph.png",
            node_name=str,
            get_depth = None
        ):
        global _node_name
        global _get_depth
        _node_name = node_name
        _get_depth = get_depth

        self.filename = filename

    def __enter__(self):
        global G
        G = nx.DiGraph()
        G.add_node(ROOT)

    def __exit__(self, exc_type, exc_val, exc_tb):
        global G

        plt.figure(figsize=(50, 24))

        pos = graphviz_layout(G, prog='dot')

        nx.draw(G,
                pos,
                with_labels=True,
                font_size=3)

        node_labels = nx.get_node_attributes(G, 'label')
        nx.draw_networkx_labels(G, pos, labels=node_labels)

        edge_labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)



        plt.savefig("Graph.png", format="PNG")
        plt.show()
