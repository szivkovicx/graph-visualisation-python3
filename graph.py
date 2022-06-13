class Graph:
    def __init__(self):
        # Node container
        self.nodes = []
        # Edge container
        self.edges = []

    ### Get a specific node by x and y coords ###
    def __get_node_by_coords__(self, x, y):
        for i in range(len(self.nodes)):
            node = self.nodes[i]

            if ('x' in node and 'y' in node):
                if (node['x'] == x and node['y'] == y):
                    return True

        return False

    ### Get a specific node using its id ###
    def __get_node_by_id__(self, id):
        for i in range(len(self.nodes)):
            node = self.nodes[i]

            if ('node' in node):
                if (node['node'] == id):
                    return True

        return False

    # Add a specific node point to the x and y coords
    def add_node(self, x, y):
        if (self.__get_node_by_coords__(x, y)):
            raise Exception('Graph error: Node with the same coordinates already exist')
        
        self.nodes.append({ "node": len(self.nodes) + 1 ,"x": x, "y": y })

    # Connect 2 node points using edge connection
    def add_edge(self, a, b):
        if (not self.__get_node_by_id__(a) or not self.__get_node_by_id__(b)):
            raise Exception("Graph error: Node with that id doesn't exist")
    
        self.edges.append({ "a": a, "b": b })
