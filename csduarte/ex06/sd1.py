# Sets variable 'x' to a string value, %d is a placeholder for a signed decimal
x = "There are %d types of people." % 10

# Sets variable 'binary' to a string value
binary = "binary"
# Sets variable 'do_not' to a string value
do_not = "don't"
# Sets variable 'y' to a string value, with two %s placeholders for strings, binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)

# sends string representation to standard out of variable x
print x
# sends string representation to standard out of variable y
print y

# sends string representation to standard out of string with a %r placeholder for representation of x
print "I said: %r." % x
# sends string representation to standard out of string with a %s placeholder for string rep of y
print "I also said: '%s'." % y

# stores value false to hilarious
hilarious = False
# stores a string value with placeholder %r in variable joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

# prints string representation of joke_evaluation, with hilarious substituted for place holder
print joke_evaluation % hilarious

#Next lines store string values in variables w & e
w = "This is the left side of..."
e = "a string with a right side"

#prints w and e, duh!
print w + e
