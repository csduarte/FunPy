# Taking 10 and injecting it in place of d
x = "There are %d types of people." % 10
# These two are variables
binary = "binary"
do_not = "don't"
# This is a variable that takes the two variables and injects them in as strings
y = "Those who know %s and those who %s." % (binary, do_not)

# Printing x and y then doing it again with more injection.
print x
print y
print "I said: %r." % x
print "I also said: '%s'." % y

# Variables again...
hilarious = False
joke_evaluation = "isn't that joke so funny?! %r"

#Looks like the % is adding the two variables together.
print joke_evaluation % hilarious

# More variables
w = "This is the left side of ..."
e = "a string with a right side."

# Print both variables with a + 
print w + e