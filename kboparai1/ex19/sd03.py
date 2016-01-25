def states_city(states, city):
    print "The states is %s and the city is %s" % (states, city) #1

print states_city("CA", "San Francisco") #2
states = "FL"
city = "Miama"
print states_city(states, city) #3
states = city
city = states
print states_city(states,city) #4

states = [
    "HA",
    "AL",
    "OH",
    "MI",
    "NY"
]

city = [
    "Maui",
    "IDK",
    "Columbus",
    "Detroit",
    "New York"
]

for (states, city) in zip(states,city):
    print states_city(states,city)
