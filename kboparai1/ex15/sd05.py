filenom = raw_input("filename > ")
txt = open(filenom)

print "Here's your file %r:" % filenom
print txt.read()

# This method is the same pretty much. 