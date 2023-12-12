class Edge:

    def __init__(self, value, distance, start_node, end_node):
        self.id = value
        self.distance = distance
        self.from_node = start_node
        self.to_node = end_node

    def get_id(self):
        return self.id

    def get_distance(self):
        return self.distance

    def get_from_node(self):
        return self.from_node

    def get_to_node(self):
        return self.to_node


if __name__ == "__main__":
    # Create nodes
    edge1 = Edge(1)
    print(edge1.get_id())
