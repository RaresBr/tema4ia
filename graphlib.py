import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()

colors = ['Red', 'Blue', 'Green']

G.add_nodes_from([4,5,6,7,1,2,3])
G.add_edges_from([(1,2),(1,3),(2,3),(2,4),(3,4),(3,5),(3,6),(4,5),(5,6)])
colors_of_nodes={}
colors_of_nodes = colors_of_nodes.fromkeys([4,5,6,7,1,2,3],None)


def is_safe(node,color):
    for neighbor in G.neighbors(node):
        neigbor_color = colors_of_nodes.get(neighbor)
        if color == neigbor_color:
            return False
    return True
def get_color_for_node(node):
    for color in colors:
        if is_safe(node,color):
            return color
def main():
    for node in G.nodes():
        colors_of_nodes[node] = get_color_for_node(node)

    print(colors_of_nodes)





def draw_stuff():
    pos=nx.spring_layout(G)
    reds = []
    for el in G.nodes():
        if colors_of_nodes[el]=='Red':
            reds.append(el)
    print('reds',reds)
    blues = []
    for el in G.nodes():
        if colors_of_nodes[el]=='Blue':
            blues.append(el)
    print('blues',blues)
    greens = []
    for el in G.nodes():
        if colors_of_nodes[el]=='Green':
            greens.append(el)
    print('greens',greens)
    nx.draw_networkx_nodes(G,pos,nodelist=reds,
                           node_color='r',
    )
    nx.draw_networkx_nodes(G,pos,nodelist=blues,
                           node_color='b',
    )
    nx.draw_networkx_nodes(G,pos,nodelist=greens,
                           node_color='g',
    )
    nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
    labels={}

    labels[1]='WA'
    labels[2]='NT'
    labels[3]='SA'
    labels[4]='Q'
    labels[5]='NSW'
    labels[6]='V'
    labels[7]='T'


    nx.draw_networkx_labels(G,pos,labels,font_size=16)

    plt.show()
# main()
# draw_stuff()
