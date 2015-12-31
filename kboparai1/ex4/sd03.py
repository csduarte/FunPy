# Cars equal to 100
cars = 100
# Space in a car equal to 4.0
space_in_a_car = 4.0
# Drivers are 30
drivers = 30
# Passengers are 90
passengers = 90
# Cars not driven are cars minus drivers
cars_not_driven = cars - drivers
# Cars driven are equal to drivers which is equal to 30
cars_driven = drivers
# Carpool capacity == uberpool
carpool_capactiy = cars_driven * space_in_a_car
# avg passengers per car is pass divided by cars driven. 
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capactiy, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."