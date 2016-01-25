from sys import argv

script, filename = argv

print "This is the file you requested %r" % filename
raw_input("Hit enter to continue")

print "Opening the file..."
target = open(filename, 'r+')

print "Reading the file."
target.read()

print "I'm going to write a line to the file."
target.write("\n")

print "Closing"
target.close()

