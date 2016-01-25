# Importing module argv from sys
from sys import argv
# Taking in script name and file name for argv
script, filename = argv
# Opening filename, which was named when invoking the script.
txt = open(filename)
# Printing filename through format variable.
print "Here's your file %r:" % filename
# prints the content of the file being read.
print txt.read()
# Collects name of file from user, aka stdin.
print "Type the filename again:"
file_again = raw_input("> ")
# Opens the filename input above.
txt_again = open(file_again)
# Prints the contents of the file being read.
print txt_again.read()