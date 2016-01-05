def a_function():
    print "Functional, not"


def b_function():
    return a_function()

b_function()


def average(*points):
    total = 0
    for p in points:
        total += p
    return total / float(len(points))

print "Average:", average(1, 2, 3, 2, 1)


