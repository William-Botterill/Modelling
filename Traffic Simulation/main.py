from node import Node
from edge import Edge
import random

Edge_List = []
Node_List = []


def main():
    # Have a look at networkX
    my_node = Node("ID: 1")
    my_edge = Edge("Edge ID: 1", 100, 1, 2)

    print("Node Value:", my_node.id)
    print("Edge: ", my_edge.id)

    for i in range(10):
        add_node(i)

    for i in range(9):
        add_edge(i, 10, i, i+1)

    print_nodes()
    print_edges()

    get_route_dfs(1, 2)

    spawn_car()


def get_max_node():
    return len(Node_List) - 1


def add_edge(edge_id, edge_length, edge_start_node, edge_end_node):
    new_edge = Edge(edge_id, edge_length, edge_start_node, edge_end_node)
    Edge_List.append(new_edge)


def add_node(node_id):
    new_node = Node(node_id)
    Node_List.append(new_node)


def print_nodes():
    print(Node_List)
    for node in Node_List:
        print("Node ID: ", node.get_id())


def print_edges():
    print("EDGE LIST")
    print(Edge_List)
    for edge in Edge_List:
        print("Edge from: ", edge.get_from_node(), " Edge to: ", edge.get_to_node())


def get_adjacent(start_id, end_id):
    adjacent = []
    for edge in Edge_List:
        if edge.get_from_node() == start_id:
            adjacent.append(edge.get_to_node())
    print(adjacent)
    return adjacent


def get_route_dfs(start_id, end_id):
    route = ""
    # get_adjacent(start_id,end_id)
    print(get_adjacent(start_id, end_id))
    return route


def spawn_car():
    print(random.randint(0, get_max_node()))


if __name__ == "__main__":
    main()
