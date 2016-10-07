#define variables
#defined cars available
cars = 100

#defined space in a car
space_in_a_car = 4.0

#defined drivers available
drivers = 30

#defined passengers available
passengers = 90

#cars without drivers
cars_not_driven = cars - drivers

#cars with drivers available
cars_driven = drivers

#carpool capacity defined by cars avaialble, plus space in each car
carpool_capacity = cars_driven * space_in_a_car

#average car utilization
average_passengers_per_car = passengers / cars_driven

#using variables
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#Study drills
#1 - Using a floating point was necessary in order to compuate averages and utilization
#2 - Floating point = accurate math capable (less rounding)
#3 - Equals is a means of assigning a variable
#4 - Underscore is a character...
#5 - Going to skip this, but understand the use of variables from algebra...