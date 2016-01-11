print "You enter a dark room with two doors.  Do you go through door #1, door #2, or door #3?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    print "3. Back away slowly."
    print "4. Shot the bear with your uzi."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good Job!"
    elif bear == "3":
        print "You back away, trip, fall on a knife and die. Sucks to be you."
    elif bear == "4":
        print "Just kidding, you left your uzi at home. So you turn around and go home."
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"

elif door == "3":
    print "You end up on the Price is Right game show, Bob Barker asked you for the price(1-1000)?"

    guess = raw_input("> ")

    if guess > 1000:
        print "The price is wrong, you die of humiliation!"
    if guess < 1:
        print "You're a idiot, your one shot and you blew it, you die of humiliation!"
    if guess == 1:
        print "That's a smart move. You won a new car! Good Job!"
    if guess > 1:
        print "You went over bid. You are left hopeless and dejected. Good job!"

else:
    print "You stumble around and fall on a knife and die.  Good job!"
