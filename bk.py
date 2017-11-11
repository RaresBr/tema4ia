from graphlib import *

def bk(asg):
    if len(get_unnassigned_nodes(asg)) == 0:
        return asg
    
    var = get_mrv_nodes(get_unnassigned_nodes(asg))[0]
    print('--------------------state info--------------------')
    print("node to assign: ", var)
    print("assigment: ",asg)
    print("----------mrv list----------")
    for i in range(0,len(get_mrv_nodes(get_unnassigned_nodes(asg)))):
        print('node',get_mrv_nodes(get_unnassigned_nodes(asg))[i])
        print('value',get_mrv(get_mrv_nodes(get_unnassigned_nodes(asg))[i]))
    print("--------------------------------------------------")
    print("unassg:", get_unnassigned_nodes(asg))
    print("mrv sorted unassg: ",get_mrv_nodes(get_unnassigned_nodes(asg)))
    for color in colors:
        print("pot sa atribui culoarea:?",color)
        index = get_index_of_node(var)
        if is_safe(list(G.nodes)[index],color):
            colors_of_nodes[list(G.nodes)[index]]=color
            if bk(asg):
                return asg
            colors_of_nodes[list(G.nodes)[index]] = None
def get_mrv(node):
    sum = 0
    for color in colors:
        if(is_safe(node,color)):
            sum = sum +1
    return sum
def get_unnassigned_nodes(nodesdict):
    lista = [item for item in nodesdict.keys() if nodesdict.get(item) == None]
    return lista
def get_mrv_nodes(nodes):
    return sorted(nodes,key = get_mrv)
def get_index_of_node(node):
    nodes = list(G.nodes())

    for i in range(0,len(nodes)) :
        if node == nodes[i]:
            return i
bk(colors_of_nodes)
print(colors_of_nodes)
draw_stuff()
for node in G.nodes():
    print(node)
print(colors_of_nodes)

