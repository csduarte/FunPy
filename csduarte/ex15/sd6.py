from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
#print txt.read()
print "File descriptor:", txt.fileno()
print "Is tty:", txt.isatty()
# print "Next:", txt.next() # can't mix with readlines
print "Readlines:", txt.readlines()
print "Tell:", txt.tell()
# print "Writing... ", txt.write("This is being read") File not open for writing
print "is closed:", txt.closed
print "encoding:", txt.encoding
print "mode:", txt.mode
print "name:", txt.name
