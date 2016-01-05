from sys import argv

script, input_file = argv

# Takes a file
def print_all(f):
    print f.read()

# takes a file
def rewind(f):
    f.seek(0)

# takes any variable, but name suggest an int and afile
def print_a_line(line_count, f):
    print line_count, f.readline()


current_file = open(input_file)

print "First let's print the whole file:\n"

# argument is a file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# argument is a file
rewind(current_file)

print "Let's print three lines:"

current_line = 1
# input is a number to print and a file
print_a_line(current_line, current_file)

current_line += 1
# input is a number to print and a file
print_a_line(current_line, current_file)

current_line += 1
# input is a number to print and a file
print_a_line(current_line, current_file)
