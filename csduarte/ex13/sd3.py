# Script takes one arugment that is an int, then ask for a multiplier, and prints out a range
# of integers multiplied

from sys import argv

args = argv

try:
    value = int(args[1])
    multiple = int(raw_input("Give me a multiple: "))

    inputs = []
    for x in range(0, value):
        print x * multiple,

except ValueError as e:
    exit("Fatal Error: First Argument was not a integer")








