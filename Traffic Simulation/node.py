class Node:
    def __init__(self, value):
        self.id = value
        self.next_node = None

    def get_id(self):
        return self.id


if __name__ == "__main__":
    # Create nodes
    node1 = Node(1)
    print(node1.get_id())
