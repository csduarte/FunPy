# IndentationError when there is no block after the if
people = 20
cats = 30
dogs = 15


if True and True:
    print "Too many cats! The world is doomed!"
#print "Too many cats! The world is doomed!"

if False and True:
    print "Not many cats! The world is saved!"
#print "Not many cats! The world is saved!"

if not(False and True):
    print "The world is drooled on!"

if not(True and True and True and True and True and True and False):
    print "The world is dry!"


dogs += 5

if 0 != 1:
    print "People are greater than or equal to dogs."

if 1 == 1:
    print "People are less than or equal to dogs."


if True or True:
    print "People are dogs."
