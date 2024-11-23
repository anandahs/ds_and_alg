def draw_pyramid(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))


height = int(input("Enter the height of the pyramid: "))
draw_pyramid(height)


def draw_pyramid(height):
    data = "*"
    for i in range(1, height + 1):
        data = "*" * (2 * i - 1)
        space = ' ' * (height - i)
        print(space + data)


draw_pyramid(6)
