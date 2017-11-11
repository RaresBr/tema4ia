graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['E'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

def find_path(graph, start, end, path=[]):
        path = path + [start]
        print(path)
        if start == end:
            return path
        if not start in graph:
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None
print(find_path(graph, 'A', 'D'))