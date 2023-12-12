from node import Node
from edge import Edge

Edge_List = []
Node_List = []


def main():
    # Have a look at networkX
    my_node = Node("ID: 1")
    my_edge = Edge("Edge ID: 1", 100, 1, 2)

    print("Node Value:", my_node.id)
    print("Edge: ", my_edge.id)


def add_edge(edge_id, edge_length, edge_start_node, edge_end_node):
    new_edge = Edge(edge_id, edge_length, edge_start_node, edge_end_node)
    Edge_List.append(new_edge)


def add_node(node_id):
    new_node = Node(node_id)
    Node_List.append(new_node)


if __name__ == "__main__":
    main()
