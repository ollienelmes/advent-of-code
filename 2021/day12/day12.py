import timeit
import networkx as nx
from networkx.algorithms import community

def path_constructor(input):
    lines = input.split("\n")
    path_dict = {}
    for line in lines:
        start, end = line.split("-")
        if start not in path_dict:
            path_dict[start] = [end]
        else:
            path_dict[start].append(end)

    return path_dict

def network_construct(input):
    nodes = []
    edges = []
    lines = input.split("\n")
    for line in lines:
        start, end = line.split("-")
        if start not in nodes:
            nodes.append(start)
        edges.append((start, end))

    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    print(nx.info(G))
    total_paths = []
    for path in nx.all_simple_paths(G, source='start', target='end'):
        total_paths.append(path)

                
    print(total_paths)
    print(len(total_paths))

def solver(dependencyDict):
    chainsDict = {}
    def get_chain_d(argDict):
        def each_path(i,caller_chain):
            a=[]
            caller_chain.append(i)
            b = argDict.get(i,[])
            for j in b:
                if j not in caller_chain:
                    a.append(j)
                    a.extend(each_path(j,caller_chain))
            return a

        return {i:each_path(i,[]) for i in argDict}

    #dependecyDict = { 'A': ['D'], 'B': ['A', 'E'], 'C': ['B'], 'D': ['C'], 'G':['H']}

    print(get_chain_d(dependencyDict))

    return chainsDict
    

if __name__ == "__main__":
    start_time = timeit.default_timer()
    with open(r'test_data1.txt', 'r') as f:
        text = f.read()
    path_dict = path_constructor(text)
    #print(path_dict)
    network_construct(text)
    print(f'Challenge 1 Answer: {solver(path_dict)}')
    #print(f'Challenge 2 Answer: {full_flash}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))