class Graph:
    def __init__(self):
        self.graph = {}

    def add_street(self, start, end, length):
        if start not in self.graph:
            self.graph[start] = []
        if end not in self.graph:
            self.graph[end] = []
        
        self.graph[start].append((end, length))
        self.graph[end].append((start, length))  # Since the graph is undirected

    def display(self):
        for corner in self.graph:
            print(f"Corner {corner}:")
            for neighbor, length in self.graph[corner]:
                print(f"  connects to {neighbor} with length {length}")

# Example usage:
graph = Graph()
graph.add_street('A', 'B', 5)
graph.add_street('A', 'C', 10)
graph.add_street('B', 'C', 7)

graph.display()