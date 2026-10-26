import os
import time


RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
BLACK = '\u001b[40m'
END = '\u001b[0m'


def clear_console():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


def flag():
    print("\nФлаг Франции:")

    width = 8
    height = 8

    for i in range(height):
        print(
            BLUE + " " * width +
            WHITE + " " * width +
            RED + " " * width +
            END
        )


def pattern_a():
    print("\nУзор a:")

    drawing = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]

    repeat_x = 3
    repeat_y = 2

    cell_width = 4
    cell_height = 2

    pattern_width = (
        repeat_x * 3 + repeat_x - 1
    ) * cell_width

    for repeat_row in range(repeat_y):
        for i in range(3):
            line = ''

            for repeat_col in range(repeat_x):
                for j in range(3):
                    if drawing[i][j] == 1:
                        line += (
                            BLACK + " " * cell_width + END
                        )
                    else:
                        line += (
                            WHITE + " " * cell_width + END
                        )

                if repeat_col < repeat_x - 1:
                    line += (
                        WHITE + " " * cell_width + END
                    )

            for k in range(cell_height):
                print(line)

        if repeat_row < repeat_y - 1:
            for k in range(cell_height):
                print(
                    WHITE + " " * pattern_width + END
                )


def animation():
    for frame in range(4):
        clear_console()

        column = frame * 4 + 1

        print(
            '\x1b[5;' + str(column) + 'H' +
            WHITE + "  " + END,
            end='',
            flush=True
        )

        time.sleep(0.4)

    clear_console()


def sequence():
    file = open('sequence.txt', 'r')

    negative = []
    positive = []

    for line in file:
        number = float(line)

        if number < 0:
            negative.append(number)

        if number > 0:
            positive.append(number)

    file.close()

    total = len(negative) + len(positive)

    print("\nДиаграмма процентов:")

    if total == 0:
        print("Нет чисел меньше или больше 0.")
    else:
        negative_percent = len(negative) / total * 100
        positive_percent = len(positive) / total * 100

        bar_width = 30

        negative_width = round(
            negative_percent / 100 * bar_width
        )

        positive_width = round(
            positive_percent / 100 * bar_width
        )

        print("Количество чисел меньше 0:")
        print(
            BLUE + " " * negative_width + END +
            " " + str(round(negative_percent, 2)) + "%"
        )

        print("Количество чисел больше 0:")
        print(
            RED + " " * positive_width + END +
            " " + str(round(positive_percent, 2)) + "%"
        )


animation()
flag()
pattern_a()
sequence()