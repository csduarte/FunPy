#inches to centimeter calculator

#variables
centimeters_per_inch = 2.54
pounds_per_kilo = 2.204
kilo_per_pound = 0.453
grams_per_kilo = 1000.0

#Describing a foot in centimeteres, using variables
print "If one inch equals %s centimeters." % centimeters_per_inch
print "Then 12 inches equals %s centimeters." % (12 * centimeters_per_inch)

#describing my weight in kilos, pounds, and grams
print "I weigh 190 pounds"
print "This means that I weigh %s kilograms" % (190.0 * kilo_per_pound)
print "Alternatively I can also say that %s is equal to %s grams" % (190.0 * kilo_per_pound, 190.0 * kilo_per_pound * grams_per_kilo)

#describing the poor use of variables
print "Most of the above is largely true, however, there are some rounding inaccuracies."
print "If I had a problem to solve, I imagine this could be much better thought out"

#common questions section
print round(1.7777)
print round(3.33)
print round(3.33) + 4.0
