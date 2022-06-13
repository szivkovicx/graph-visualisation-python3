import random
from graph import Graph
from matplotlib import pyplot as plt
from config import GRAPH_CONNECTION_RATE, SAMPLE_SIZE

###  Generate chunks with n length of child elements ###
def chunks(lst, n):
    return [lst[i:i+2] for i in range(0,len(lst),n)]

### Shuffle wrapper for random shuffle ###
def shuffle(arr):
    random.shuffle(arr)
    return arr

### Node filtering function ###
def filter(arr, id):
    for i in range(len(arr)):
        e = arr[i]
        
        if (e["node"] == id):
            return e
    
    return None

### Create graph and fill it with random nodes and edges ###
def create_graph():
    graph = Graph()

    # Generate coords
    coords = chunks(random.sample(range(SAMPLE_SIZE), int(SAMPLE_SIZE/5)), 2)

    # Generate nodes based on coords
    for i in range(len(coords)):
        x, y = coords[i]

        graph.add_node(x, y)

    # For a particular graph connection rate generate random edge connections
    for y in range(GRAPH_CONNECTION_RATE):
        ids = chunks(shuffle(list(range(1, len(graph.nodes) + 1))), 2)
        for i in range(len(ids)):
            a, b = ids[i]

            graph.add_edge(a, b)

    # Return graph
    return graph

### Visualise the graph object ###
def plot_graph(graph):
    x1 = [filter(graph.nodes, edge["a"])["x"] for edge in graph.edges]
    x2 = [filter(graph.nodes, edge["b"])["x"] for edge in graph.edges]
    y1 = [filter(graph.nodes, edge["a"])["y"] for edge in graph.edges]
    y2 = [filter(graph.nodes, edge["b"])["y"] for edge in graph.edges]

    plt.xlim(0, SAMPLE_SIZE)
    plt.ylim(0, SAMPLE_SIZE)

    plt.plot(x1, y1, x2, y2, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")

    plt.show()
