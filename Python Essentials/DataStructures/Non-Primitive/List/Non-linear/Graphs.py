graph ={ 'a': ['c', 'd'],
         "b":['d','e'],
         "c":['a','e'],
         "d":['a','b'],
         "e":['b','c'],
         }

def define_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges

print(define_edges(graph))