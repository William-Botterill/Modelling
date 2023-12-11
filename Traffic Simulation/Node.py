class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def get_value(self):
        return self.value


if __name__ == "__main__":
    # Create nodes
    node1 = Node(1)
    print(node1.get_value())
