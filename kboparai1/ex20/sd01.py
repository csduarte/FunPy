from sys import argv

script, input_file = argv
# def print_all that takes the f and reads it.
def print_all(f):
    print f.read()
# def rewind that take the f and seek @ 0
def rewind(f):
    f.seek(0)
# def that takes in linecount and f. then reads that line of that file f.
def print_a_line(line_count, f):
    print line_count, f.readline()
# var to open input file
current_file = open(input_file)

print "First let's print the whole file:\n"
# opens currentfile and then reads it. so it looks like open(current_file).read()
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# open(current_file).seek(0)
rewind(current_file)

print "Let's print three lines:"
# set to read line 1 of current file
current_line = 1
print_a_line(current_line, current_file)
# set to read line current_line + 1 of current file happens to be 2
current_line = current_line + 1
print_a_line(current_line, current_file)
# set to read line current_line + 1 of current file happens to be 3
current_line = current_line + 1
print_a_line(current_line, current_file)