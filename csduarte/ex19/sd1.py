# Function that takes two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # String to STDOUT, with signed decimal placeholder
    print "You have %d cheeses!" % cheese_count
    # String to STDOUT, with signed decimal placeholder
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # String to STDOUT
    print "Man that's enough for a party!"
    # String to STDOUT
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
# Call function with cheese_count set to 30, boxes_of_crackers 30
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
# Sets two variables
amount_of_cheese = 10
amount_of_crackers = 50
# Call function with cheese_count with value of variable, boxes_of_crackers with value of variable
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# Call function with cheese_count set to 10 + 20, boxes_of_crackers 5 + 6
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
# Call function with cheese_count set to variable + 100, boxes_of_crackers variable + 1000
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
