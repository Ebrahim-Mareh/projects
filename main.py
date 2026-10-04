import os
import time


# France flag

print("\033[44m      \033[47m      \033[41m      \033[0m")
print("\033[44m      \033[47m      \033[41m      \033[0m")
print("\033[44m      \033[47m      \033[41m      \033[0m")
print("\033[44m      \033[47m      \033[41m      \033[0m")
print("\033[44m      \033[47m      \033[41m      \033[0m")
print("\033[44m      \033[47m      \033[41m      \033[0m")
print("\033[44m      \033[47m      \033[41m      \033[0m")
print("\033[44m      \033[47m      \033[41m      \033[0m")


# Pattern a

print()
print("██  ██    ██  ██")
print("  ██        ██")
print("██  ██    ██  ██")


# Animation

time.sleep(1)

os.system("cls")
print("\033[5;5H*")
time.sleep(0.5)

os.system("cls")
print("\033[5;10H*")
time.sleep(0.5)

os.system("cls")
print("\033[5;15H*")
time.sleep(0.5)

os.system("cls")
print("\033[5;20H*")
time.sleep(0.5)


# Sequence

file = open("sequence.txt", "r")

negative = 0
positive = 0

for number in file:
    number = float(number)

    if number < 0:
        negative = negative + 1

    if number > 0:
        positive = positive + 1

file.close()


print()
print("Negative:", negative)
print("Positive:", positive)


# Percentages

total = negative + positive

negative_percent = negative / total * 100
positive_percent = positive / total * 100

print("\033[44m" + " " * int(negative / 5) + "\033[0m",
      negative_percent, "%")

print("\033[41m" + " " * int(positive / 5) + "\033[0m",
      positive_percent, "%")