# Execute using Fn+Shift+F10
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def main():
    # Total area will have height 3 and width 5 making total area 15
    # Any coordinate that is within (x - 1.5)^2 + (y - 1.5)^2 < 1 will be within the circle of radius 1
    # Any coordinate that is within 3 < x < 4 and 1 < y < 2 will be a part of the square

    square_count = 0
    circle_count = 0
    area_count = 0

    for i in range(5000000):
        x = random.uniform(0, 3.01)
        y = random.uniform(0, 2)

        if (x - 1) ** 2 + (y - 1) ** 2 < 1:
            circle_count += 1
        elif 2.01 <= x <= 3.01 and 0 <= y <= 1:
            square_count += 1
        else:
            area_count += 1

    print("Square Count: ", square_count)
    print("Area Count: ", area_count)
    print("CircleCount: ", circle_count)
    print("PI Estimate", circle_count / square_count)


if __name__ == '__main__':
    main()
