import math
import os


def circle_area(radius):
    return math.pi * radius ** 2


def square_area(side_length):
    return side_length ** 2


def triangle_area(base, height):
    return 0.5 * base * height


def rect_area(length, width):
    return length * width


def Console(command):
    os.system(command)


def main():
    Console("clear")
    choice = 0

    print("Geometrical Shapes Area Calculator")
    print("=====================================")
    print()
    print("1.\tCircle")
    print("2.\tTriangle")
    print("3.\tSquare")
    print("4.\tRectangle")
    print("5.\tQuit")
    print()

    while choice != 5:
        choice = int(input("Please choose a shape from 1-4: "))

        if choice == 1:
            radius = float(input("\n> Enter radius of circle: "))
            area = circle_area(radius)
            print("\nThe area is: %.2f" % area)
            print()
        elif choice == 2:
            base = float(input("\n> Enter base of triangle: "))
            height = float(input("> Enter height of triangle: "))
            area = triangle_area(base, height)
            print("\nThe area is: %.2f" % area)
            print()
        elif choice == 3:
            side_length = float(input("\n> Enter side length of square: "))
            area = square_area(side_length)
            print("\nThe area is: %.2f" % area)
            print()
        elif choice == 4:
            length = float(input("\n> Enter length of rectangle: "))
            width = float(input("> Enter width of rectangle: "))
            area = rect_area(length, width)
            print("\nThe area is: %.2f" % area)
            print()
        else:
            print("\nExitting...")


if __name__ == "__main__":
    main()
