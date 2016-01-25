from sys import exit

#I'm going to add to it, simplifying is for suckers ;)

def gold_room():
    print "This room is full of gold.  How much do you take?"

    next = raw_input("> ")
    if "0" is next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu"
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print "You died.  But strangely your inner dialog is still going."
    print "Something is happening.  Like to that one kid in the book.  You're going to see Heaven."
    print "Instead you are presented with a big white pearly gate."
    print "Saint Peter stands a head higher and stares you down like a Mexican gangster"
    print "What do you have to say for yourself?"

    statement = raw_input("> ")

    if "sorry" in statement:
        print "Saint Peter likes that you have repented and opens the gates."
        print "In the distance you see a professional beach ball tournament staring soon."
        print "Even better, you get the scent of the most perfect Chinese/Japanese Buffet. Yum!"
        print "Good job!"
    else:
        print "Saint Peter pulls out his red marker and crosses your name off the clipboard"
        print "You have a feeling of dread.  The world blurs and you feel nauseous."
        print "When the spinning stops, you're in the forrest.   Upon further inspection..."
        print "You seem to be a banana slug. Cool!"
        print "But wait! A swishing noise signals a boot bringing your impending doom."
        print "Squish!! You're really dead this time. Good job!"
    exit(0)


def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
