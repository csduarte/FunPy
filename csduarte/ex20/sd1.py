# Imports argv property from the sys module
from sys import argv

# Unpacks script and first argument into variables
script, input_file = argv

# Creates function that reads content of a file and prints it to standard out
def print_all(f):
    print f.read()

# Defines function that moves file position to byte offset zero
def rewind(f):
    f.seek(0)

# Defines a function that prints a line count from argument and reads next line of a file
def print_a_line(line_count, f):
    print line_count, f.readline()

# Creates a file object to manipulate
current_file = open(input_file)

# Print a string
print "First let's print the whole file:\n"

# Calls the 'print_all' function with the current file
print_all(current_file)

# Print a string
print "Now let's rewind, kind of like a tape."

# Calls the 'rewind' function with the current file
rewind(current_file)

# Print a string
print "Let's print three lines:"

# Set variable to '1'
current_line = 1

# calls 'print_a_line' function with the cl variable and cf
print_a_line(current_line, current_file)

# Set variable to current value + 1
current_line += 1

# calls 'print_a_line' function with the cl variable and cf
print_a_line(current_line, current_file)

# Set variable to current value + 1
current_line += 1

# calls 'print_a_line' function with the cl variable and cf
print_a_line(current_line, current_file)
