def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b


def subtract(a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b


def multiply(a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b


def divide(a, b):
    print "Dividing %d / %d" % (a, b)
    return a / b

print "let's do some math with just functions!"

age = add(30, 5)  # 35
height = subtract(78, 4)  # 74
weight = multiply(90, 2)  # 180
iq = divide(100, 2)  # 50

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

# Reversed the functions, not going to do the math again, i'll let python do it.
# Added a float so it wouldn't be a boring zero after the value became less than 1
what = divide(age, float(multiply(height, subtract(weight, add(iq, 2)))))

print "That becomes: ", what, "Can you do it by hand?"