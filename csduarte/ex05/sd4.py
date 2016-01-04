my_name = "Zed A. Shaw"
my_age = 35
# Inches
my_height = 74
# Centimeters
my_weight = 180
my_eyes = "Blue"
my_teeth = "White"
my_hair = "Brown"


def inches_to_centimeter(inches=0):
    return inches * 2.54


def pounds_to_kilos(pounds=0):
    return pounds / 2.2046

print "Let's talk about %s." % my_name
print "He's %d centimeters tall." % inches_to_centimeter(my_height)
print "He's %d kilograms heavy." % pounds_to_kilos(my_weight)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usual %s depending on the coffee." % my_teeth

print "If I add %d, %d, and %d I get %d." % (
    my_age, inches_to_centimeter(my_height), pounds_to_kilos(my_weight),
    my_age + inches_to_centimeter(my_height) + pounds_to_kilos(my_weight))
