import os
import time


RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
BLACK = '\u001b[40m'
END = '\u001b[0m'


def clear_console():
  os.system("cls")
   


def flag():
    clear_console()
    print("\nFrench Flag:")

    for i in range(8):
        print(BLUE + " " * 8+
              WHITE + " " * 8 +
              RED + " " * 8+ END)



    input("\nPress Enter to continue...")


def pattern_a():
    clear_console()
    print("\nPattern a:")

    drawing = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]

    cell_width = 4
    cell_height = 2

    separator = WHITE + " " * cell_width + END

    for i in range(len(drawing)):
        line = ""

        for j in range(len(drawing[i])):
            if drawing[i][j] == 1:
                line += BLACK + " " * cell_width + END
            else:
                line += WHITE + " " * cell_width + END

        # نضع نسختين بجانب بعضهما
        line = line + separator + line

        for k in range(cell_height):
            print(line)
    input("\nPress Enter to continue...")


def animation():
    for column in [1, 5, 9, 13]:
        clear_console()

        print('\x1b[5;' + str(column) + 'H' + WHITE + "  " + END,
              end='', flush=True)

        time.sleep(0.4)

    clear_console()
    print("Animation finished.")
    input("\nPress Enter to continue...")


def sequence():
    clear_console()

    positive = 0
    negative = 0

    file = open("sequence.txt", "r")

    for line in file:
       
        if float(line) > 0:
            positive += 1
        elif float(line) < 0:
            negative += 1

    file.close()

    total = positive + negative

    if total != 0:

        p = positive / total * 100
        n = negative / total * 100 

      

        print("\nPositive numbers:")
        print(RED + " " * round(p * 30 / 100) + END, p, "%")


        print("\nNegative numbers:")
        print(BLUE + " " * round(n * 30 / 100) + END, n, "%")

    input("\nPress Enter to finish...")

def function_graph():
    graph = "\x1b[2J\x1b[H"

    for row in range(2, 22):
        graph += "\x1b[" + str(row) + ";2H|"

    for column in range(2, 42):
        graph += "\x1b[21;" + str(column) + "H-"

    for step in range(40):
        x = step / 6
        y = x * x

        row = 21 - round(y)
        column = step + 2

        graph += "\x1b[" + str(row) + ";" + str(column) + "H*"

    graph += "\x1b[23;1H"
    print(graph, end="")


    input("\nPress Enter to exit...") 
    clear_console()



flag()
pattern_a()
animation()
sequence()
function_graph()