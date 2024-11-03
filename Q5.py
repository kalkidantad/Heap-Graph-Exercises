class Node:
    def __init__(self, val):
        self.val = val
        self.adjacent = []


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, val):
        if val not in self.nodes:
            self.nodes[val] = Node(val)

    def add_edge(self, n1, n2):
        if n1 not in self.nodes:
            self.add_node(n1)
        if n2 not in self.nodes:
            self.add_node(n2)
        self.nodes[n1].adjacent.append(self.nodes[n2])

    def print_graph(self):
        for node in self.nodes.values():
            print(f"Node {node.val} shares an edge -")
            for neighbor in node.adjacent:
                print(f"-> Node {neighbor.val}")

"""it opens cities.txt, skips the header line, and reads each subsequent line. For each line, splits the text into source and destination city names, and then calls add_edge to add a directed edge from source to destination."""

def build_graph(filename):
    graph = Graph()
    with open(filename, 'r') as file:
        next(file)  
        for line in file:
            source, destination = line.strip().split(',')
            graph.add_edge(source, destination)
    return graph


graph = build_graph('cities.txt')
graph.print_graph()
