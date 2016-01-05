from sys import argv

script, first, second, third = argv
fourth = raw_input("fourth? ")

print "Well %r, then %r, ok so %r, oh then %r, lastly.. %r" % (script, first, second, third, fourth)