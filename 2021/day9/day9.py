import timeit
import networkx as nx
from networkx.algorithms import community
def input_cleaner(text):
    lines = text.split("\n")
    line_grid = []
    for line in lines:
        line_list = []
        for num in line:
            line_list.append(int(num))
        line_grid.append(line_list)

    return line_grid

def low_point_finder(line_grid):
    risk_count = 0
    for line_index in range(len(line_grid)):
        #the first line
        if line_index == 0:
            for num_index in range(len(line_grid[line_index])):
                #number is on the far left
                if num_index == 0:
                    if line_grid[line_index][num_index] < line_grid[line_index][num_index + 1] and line_grid[line_index][num_index] < line_grid[line_index+1][num_index]:
                        risk_count += 1 + line_grid[line_index][num_index]
                #number is on the far right of the grid
                elif num_index == (len(line_grid[line_index])-1):
                    if line_grid[line_index][num_index] < line_grid[line_index][num_index - 1] and line_grid[line_index][num_index] < line_grid[line_index+1][num_index]:
                        risk_count += 1 + line_grid[line_index][num_index]
                else:
                    if line_grid[line_index][num_index] < line_grid[line_index][num_index + 1] and line_grid[line_index][num_index] < line_grid[line_index][num_index-1] and line_grid[line_index][num_index] < line_grid[line_index+1][num_index]:
                        risk_count += 1 + line_grid[line_index][num_index]
        #the last line
        elif line_index == (len(line_grid)-1):
            for num_index in range(len(line_grid[line_index])):
                #number is on the far left
                if num_index == 0:
                    if line_grid[line_index][num_index] < line_grid[line_index][num_index + 1] and line_grid[line_index][num_index] < line_grid[line_index-1][num_index]:
                        risk_count += 1 + line_grid[line_index][num_index]
                #number is on the far right of the grid
                elif num_index == (len(line_grid[line_index])-1):
                    if line_grid[line_index][num_index] < line_grid[line_index][num_index - 1] and line_grid[line_index][num_index] < line_grid[line_index-1][num_index]:
                        risk_count += 1 + line_grid[line_index][num_index]
                else:
                    if line_grid[line_index][num_index] < line_grid[line_index][num_index + 1] and line_grid[line_index][num_index] < line_grid[line_index][num_index-1] and line_grid[line_index][num_index] < line_grid[line_index-1][num_index]:
                        risk_count += 1 + line_grid[line_index][num_index]
        #middle sections
        else:
            for num_index in range(len(line_grid[line_index])):
                #number is on the far left
                if num_index == 0:
                    if line_grid[line_index][num_index] < line_grid[line_index][num_index + 1] and line_grid[line_index][num_index] < line_grid[line_index-1][num_index] and line_grid[line_index][num_index] < line_grid[line_index+1][num_index]:
                        risk_count += 1 + line_grid[line_index][num_index]
                #number is on the far right of the grid
                elif num_index == (len(line_grid[line_index])-1):
                    if line_grid[line_index][num_index] < line_grid[line_index][num_index - 1] and line_grid[line_index][num_index] < line_grid[line_index-1][num_index] and line_grid[line_index][num_index] < line_grid[line_index+1][num_index]:
                        risk_count += 1 + line_grid[line_index][num_index]
                else:
                    if line_grid[line_index][num_index] < line_grid[line_index][num_index - 1] and line_grid[line_index][num_index] < line_grid[line_index][num_index + 1] and line_grid[line_index][num_index] < line_grid[line_index-1][num_index] and line_grid[line_index][num_index] < line_grid[line_index+1][num_index]:
                        risk_count += 1 + line_grid[line_index][num_index]
                

    return risk_count
def node_list(line_grid):
    co_ord_list = []
    for line_index in range(len(line_grid)):    
        for num_index in range(len(line_grid[line_index])):
            if line_grid[line_index][num_index] != 9:
                co_ord_list.append(str(line_index) + " " + str(num_index))
    return co_ord_list

def edge_list(line_grid):
    edge_list = {'source': [], 'target': []}
    for line_index in range(len(line_grid)):    
        for num_index in range(len(line_grid[line_index])):
            if line_grid[line_index][num_index] != 9:
                if num_index != len(line_grid[line_index])-1:
                    if line_grid[line_index][num_index] < line_grid[line_index][num_index + 1] and line_grid[line_index][num_index+1] != 9:
                        edge_list['source'].append(str(line_index) + " " + str(num_index))
                        edge_list['target'].append(str(line_index) + " " + str(num_index+1))
                if num_index != 0:
                    if line_grid[line_index][num_index] < line_grid[line_index][num_index -1] and line_grid[line_index][num_index-1] != 9:
                        edge_list['source'].append(str(line_index) + " " + str(num_index))
                        edge_list['target'].append(str(line_index) + " " + str(num_index -1))
                if line_index != len(line_grid)-1:
                    if line_grid[line_index][num_index] < line_grid[line_index+1][num_index] and line_grid[line_index+1][num_index] != 9:
                        edge_list['source'].append(str(line_index) + " " + str(num_index))
                        edge_list['target'].append(str(line_index+1) + " " + str(num_index))
                if line_index != 0:
                    if line_grid[line_index][num_index] < line_grid[line_index-1][num_index] and line_grid[line_index-1][num_index] != 9:
                        edge_list['source'].append(str(line_index) + " " + str(num_index))
                        edge_list['target'].append(str(line_index-1) + " " + str(num_index))

    return edge_list

def gen_network(edge_dict, node_list):
    edges = []
    print(len(edge_dict['source']))
    for i in range(len(edge_dict['source'])):
        edges.append((edge_dict['source'][i], edge_dict['target'][i]))
    #print(edges)
    G = nx.Graph()
    G.add_nodes_from(node_list)
    G.add_edges_from(edges)
    #print(nx.info(G))
    list_comp = [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
    final_val = list_comp[0] * list_comp[1] * list_comp[2]
   
    return final_val
        
if __name__ == "__main__":
    start_time = timeit.default_timer()
    with open(r'input9.txt', 'r') as f:
        text = f.read()
    line_grid = input_cleaner(text)
    list_of_nodes = node_list(line_grid)
    list_of_edges = edge_list(line_grid)
    print(f'Challenge 1 Answer: {low_point_finder(line_grid)}')
    print(f'Challenge 2 Answer: {gen_network(list_of_edges, list_of_nodes)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))