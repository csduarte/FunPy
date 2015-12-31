# The amount of cars
cars = 100

# This space in a car
space_in_a_car = 4.0

# The amount of drivers
drivers = 30

# Amount of non-drivers
passengers = 90

# Amount of unused cars
cars_not_driven = cars - drivers

# Amount of used cars
cars_driven = drivers

# Total Capacity
carpool_capacity = cars_driven * space_in_a_car

# Non-Drivers per car
average_passenger_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today."
print "we can transport", carpool_capacity, "people today."
print "we have", passengers, "to carpool today"
print "We need to put about", average_passenger_per_car, "in each car."
