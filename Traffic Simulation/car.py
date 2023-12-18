import threading
import main


def find_route():
    main.get_route_dfs(1, 2)


class Car:
    def __init__(self, value, speed, start, end):
        self.id = value
        self.speed = speed
        self.start = start
        self.end = end
        self. position = 0

    def get_id(self):
        return self.id

    def get_speed(self):
        return self.speed

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    # def drive(self):




if __name__ == "__main__":
    # Create nodes
    node1 = Car(1, 5, 2, 3)
    print(node1.get_id())
