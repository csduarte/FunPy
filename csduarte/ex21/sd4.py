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

# Formula
x = 22 * 49 + 1 - 99 / 100 * 1800
# PEMDAS

print "x: ", x
print "Functional: ", subtract(add(multiply(22, 49), 1), divide(99, multiply(100, 1800)))

