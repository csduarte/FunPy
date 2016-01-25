# Gold room has issues with number checking. Numbers can have digits 0-9, not just 0 and 1

# A better way would be to use a try-catch block


def input_number():
    try:
        print "Please type a number."
        value = int(raw_input("> "))
    except ValueError:
        print "Learn to type a number, (wo)man!"
        input_number()
    else:
        print "Good job! You're #%d on the best people list." % value

input_number()