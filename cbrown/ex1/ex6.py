#Using a string to input 10 into the x variable
x = "There are %d types of people." % 10

#defining binary
binary = "binary"

#defining don't
do_not = "don't"

#defining y, using two strings to reference the binary and do_not variables
y = "Those who know %s and those who %s." % (binary, do_not)

#printing variable x
print x

#printing variable y
print y

#printing a joke using strings and defined variables
print "I said: %r." % x
print "I also said: '%s'." % y

#defining hilarious as false
hilarious = False

#holy shit - finally figured this out
#defining a variable, with an embedded string!
joke_evaluation = "Isn't that joke so funny?! %r"

#printing the joke_evaluation variable and inputting the hilarious variable to finish the string
print joke_evaluation % hilarious

#defining w and e variables with text
w = "This is the left side of..."
e = "a string with a right side."

#printing variables w and e to make a sentence
print w + e