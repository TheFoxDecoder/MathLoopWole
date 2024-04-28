import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

class Loopwhole:
    def __init__(self):
        self.arr = []
        self.graph = nx.DiGraph()
        self.run()
    
    @staticmethod
    def check(x):
        if x % 2 == 0: # even 
            return x / 2
        else: # odd
            return x * 3 + 1
    
    def loop(self, x):        
        linked_list = LinkedList()
        while True:
            linked_list.append(x)
            self.graph.add_node(x)
            z = self.check(x)
            self.graph.add_edge(x, z)
            if z == 1: # last destination 
                return
            else:
                x = z
                self.arr.append(z)
        
    def run(self):
        # loop that needs to function  
        x = int(input("Enter number: "))
        self.loop(x)

        # Visualize the graph
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, arrows=True)
        plt.savefig('collatz_graph.png')  # Save the plot
        plt.show()

if __name__ == "__main__":
    Loopwhole()
