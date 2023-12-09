# Execute using Fn+Shift+F10
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
from tkinter import *

root = Tk()


def show_output():
    root.title("Monte Carlo Area Simulation")
    root.configure(background="green")
    root.minsize(300, 200)
    root.maxsize(1200, 1000)
    root.geometry("1000x600+100+100")

    canvas = Canvas(root, width=800, height=520)
    canvas.create_oval(10, 10, 510, 510, outline='black', fill='white')
    canvas.create_rectangle(520, 10, 770, 260)
    canvas.place(x=100, y=50)
    refresh = Button(root, text="Refresh Points", command=lambda: draw_points(canvas))
    refresh.place(x=100, y=20)
    draw_points(canvas)
    root.mainloop()


def show_statistics(square_count, circle_count, area_count):
    square_label = Label(root, text="Square Count: " + str(square_count))
    square_label.place(x=200, y=20)
    circle_label = Label(root, text="Circle Count: " + str(circle_count))
    circle_label.place(x=350, y=20)
    area_label = Label(root, text="Area Count: " + str(area_count))
    area_label.place(x=500, y=20)
    pi_estimate_label = Label(root, text="PI Estimation: " + str(circle_count/square_count))
    pi_estimate_label.place(x=650, y=20)
    print("Square Count: ", square_count)
    print("Area Count: ", area_count)
    print("CircleCount: ", circle_count)
    print("PI Estimate", circle_count / square_count)


def draw_points(canvas):
    # Total area will have height 3 and width 5 making total area 15
    # Any coordinate that is within (x - 1.5)^2 + (y - 1.5)^2 < 1 will be within the circle of radius 1
    # Any coordinate that is within 3 < x < 4 and 1 < y < 2 will be a part of the square
    canvas.delete("all")

    square_count = 0
    circle_count = 0
    area_count = 0

    for i in range(50000):
        x = random.uniform(0, 800)
        y = random.uniform(0, 520)

        if (x - 260) ** 2 + (y - 260) ** 2 < 250 ** 2:
            circle_count += 1
            canvas.create_oval(x, y, x + 1, y + 1, fill="blue")
        elif 520 <= x <= 770 and 10 <= y <= 260:
            square_count += 1
            canvas.create_oval(x, y, x + 1, y + 1, fill="green")
        else:
            area_count += 1
            canvas.create_oval(x, y, x + 1, y + 1)
    show_statistics(square_count, circle_count, area_count)


def main():
    show_output()


if __name__ == '__main__':
    main()
