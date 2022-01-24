def aStarAlgo(start_node,stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node
    
    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n == None or g[v]+heuristic(v) < g[n]+heuristic(n):
                n= v
        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m,weight) in get_neighbors(v):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
                if n == None:
                    print('path doesnt exist !')
                    return None
                if n == stop_node:
                    path = []
                    while parents[n]!=n:
                        path.append(n)
                        n = parents[n]
                    path.append(start_node)
                    path.reverse()
                    print('Path found : {}'.format(path))
                    return path
                open_set.remove(n)
                closed_set.add(n)
         
        print('Path doesnt exist !')
        return None
    
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None
    
def heuristic(n):
    H_dist = {
        'A':5,
        'B':6,
        'C':8,
        'D':2,
        'E':4,
        'F':1,
        'G':9,
        'H':4,
        'I':7,
        'J':6,
    }
    return H_dist[n]

Graph_nodes = {
    'A':[('B',5),('C',8)],
    'B':[('C',5),('F',8)],
    'C':[('A',2),('B',2)],
    'D':[('G',5),('C',8)],
    'E':[('D',5),('C',8)],
    'F':[('E',8)],
    'G':[('B',5),('C',8)],
    'H':[('B',5),('C',8)],
    'I':[('B',5),('C',8)],
}
aStarAlgo('A','J')
                
