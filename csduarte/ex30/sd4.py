# Variable Assignments
people = 30
cars = 40
buses = 15

# When Cars greater than people value
if cars > people:
        print "We should take the cars."
# When Cars less than people value
elif cars < people:
        print "We should not take the cars."
# When any of the preceding conditions failed
else:
    print "We can't decide."

# When buses value is greather than cars value
if buses > cars:
    print "That's too many buses."
# When buses value is less than cars value
elif buses < cars:
    print "Maybe we could take the buses."
# When the preceding conditions failed
else:
    print "We still can't decide."

# When the people value is greater than the buses value
if people > buses:
    print "Alright, let's just take the buses."
# When the previous condition is not true
else:
    print "Fine, let's stay home then."
