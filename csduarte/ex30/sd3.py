people = 30
cars = 30
buses = 30


if True and people > cars > buses:
        print "We should take the cars."
elif False and buses > cars > people:
        print "We should not take the cars."
else:
    print "We can't decide."


if not(people <= cars):
    print "That's too many buses."
elif buses > cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."


if people == cars == buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."
