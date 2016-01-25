# This is a def named cheese_and_crackers. It wants two values, cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # format variables for cheese_count
    print "You have %d cheeses!" % cheese_count
    # for boxes of crackers
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# Now adds 20 and 30 to the def and fills out the format variables.
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# Throwing in variables in for the def. Pretty much the same thing as putting in 20,30
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# adding variables so not 30, 11
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# 110,1050
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)