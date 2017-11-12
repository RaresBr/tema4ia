from graphlib import *
import copy

def bk(asg):
    if len(get_unassigned_nodes(asg)) == 0:
        return asg
    
    var = get_mrv_nodes(get_unassigned_nodes(asg))[0]
    print('--------------------state info--------------------')
    print("node to assign: ", var)
    print("assigment: ",asg)
    print("----------mrv list----------")
    for i in range(0,len(get_mrv_nodes(get_unassigned_nodes(asg)))):
        print('node',get_mrv_nodes(get_unassigned_nodes(asg))[i])
        print('value',get_mrv(get_mrv_nodes(get_unassigned_nodes(asg))[i]))
    print("--------------------------------------------------")
    print("unassg:", get_unassigned_nodes(asg))
    print("mrv sorted unassg: ",get_mrv_nodes(get_unassigned_nodes(asg)))
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
        if is_safe(node,color):
            sum = sum +1
    return sum
def get_unassigned_nodes(nodesdict):
    lista = [item for item in nodesdict.keys() if nodesdict.get(item) == None]
    return lista
def get_mrv_nodes(nodes):
    return sorted(nodes,key = get_mrv)
def get_index_of_node(node):
    nodes = list(G.nodes())

    for i in range(0,len(nodes)) :
        if node == nodes[i]:
            return i
def get_domain(node):
    domain = []
    for color in colors:
        if is_safe(node,color):
            domain.append(color)
    return domain
def get_all_domains():
    domains = []
    for node in G.nodes():
        domains.append(get_domain(node))
    return domains
def get_unassigned_neighbors(node,nodesdict):
    unasg = get_unassigned_nodes(nodesdict)
    unasg_neighbors = []
    all_neighbors = G.neighbors(node)
    for neighbor in all_neighbors:
        if neighbor in unasg:
            unasg_neighbors.append(neighbor)
    return unasg_neighbors
def forward_check(asg,domains):
    if len(get_unassigned_nodes(asg))==0:
        return asg
    node = get_unassigned_nodes(asg)[0]
    index = get_index_of_node(node)
    for color in domains[index]:
        if is_safe(node,color):
            colors_of_nodes[list(G.nodes)[index]]=color
            domains_copy = copy.deepcopy(domains)
            for unassigned_neighbor in get_unassigned_neighbors(node,asg):
                for color in domains_copy[get_index_of_node(unassigned_neighbor)]:
                    if not is_safe(unassigned_neighbor,color):
                        domains_copy[get_index_of_node(unassigned_neighbor)].remove(color)
            all_neighbors_not_empty = True
            for unassigned_neighbor in get_unassigned_neighbors(node,asg):
                if len(domains_copy[get_index_of_node(unassigned_neighbor)]) == 0:
                    all_neighbors_not_empty = False
                    break
            if all_neighbors_not_empty == True:
                result = forward_check(asg,domains_copy)
                if result is not None:
                    return result
            colors_of_nodes[list(G.nodes)[index]] = None
    return None


# print(get_all_domains())
# colors_of_nodes[1]='Red'
# dc = copy.deepcopy(get_all_domains())
# for node in G.nodes():
    # dc[get_index_of_node(node)].remove('Green')
    # if len(dc[get_index_of_node(node)]) != 0:
        # print('not empty')
    # else:
        # print('empty')
    # print(node,get_index_of_node(node),dc[get_index_of_node(node)])
    
# forward_check(colors_of_nodes,get_all_domains())

# bk(colors_of_nodes)
print(colors_of_nodes)
draw_stuff()

# for node in G.nodes():
    # print(node)
# print(colors_of_nodes)

