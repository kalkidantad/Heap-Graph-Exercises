
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

    def add_edge(self,n1,n2):
        if n1 not in self.nodes:
            self.add_node(n1)
        if n2 not in self.nodes:
            self.add_node(n2)

        self.nodes[n1].adjacent.append(self.nodes[n2])

        
    """ it uses queue that is a list which holds tuples containing node object and a list to represent the path taken. it uses visited set to track visited nodes"""
    
    def breadth_fs(self, start, goal):
        if start not in self.nodes or goal not in self.nodes:
            print("The given start or goal does not exist in the cities ")
            return 
        queue = [(self.nodes[start], [start])]
        visited = set()

        while queue:
            current , path = queue.pop(0)
            if current.val == goal:
                print("BFS Path","->".join(path))
                return
            visited.add(current.val)

            for neighbor in current.adjacent:
                if neighbor.val not in visited:
                    queue.append((neighbor, path +[neighbor.val]))

    print("No path from the starting to the goal node ")



    def recursive_dfs(self, start,goal):
        if start not in self.nodes or goal not in self.nodes:
            print("The given start or goal does not exist in the cities")
            return
        visited = set()
        path = self.recursive (self.nodes[start], goal, visited, [start])
        if path:
            print("DFS Path","->".join(path))

        else:
            print("No path from the starting to the goal node ")

    
    def recursive(self, node, goal, visited, path):
        if node.val == goal:
            return path
        visited.add(node.val)

        for neieghbor in node.adjacent:
            if neieghbor.val not in visited:
                result = self.recursive(neieghbor,goal,visited,path +[neieghbor.val])
                if result:
                    return result
                
        return None
    
def build_graph(filename):
    graph = Graph()
    with open(filename, 'r') as file:
        next(file)  
        for line in file:
            source, destination = line.strip().split(',')
            graph.add_edge(source, destination)
    return graph

graph = build_graph('cities.txt')
graph.breadth_fs('New York','Chicago')
graph.breadth_fs('Houston','Boston')