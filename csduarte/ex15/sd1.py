# imports the argv function from the sys module
from sys import argv

# unpacks argv into the script running on the first argument
script, filename = argv

# open the file provided
txt = open(filename)

# Prints a string out with the placeholder %r, repr() of filename
print "Here's your file %r:" % filename
# calls the read function of the txt object
print txt.read()

# Prints a string to standard out
print "Type the filename again:"
# prints out the string ("> ") and reads in the next line from user
file_again = raw_input("> ")

# opens file by the string
txt_again = open(file_again)

# prints out the result of calling the read function from the opened file
print txt_again.read()
