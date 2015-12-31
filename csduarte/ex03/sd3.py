#Gravitational Pull Between Earth and Moon
EARTH_MASS = 5.974 * 10**24
MOON_MASS = 7.349 * 10**22
G = 6.674 * 10**-11
R = 3.844 * 10**8

attraction = (G * MOON_MASS * EARTH_MASS) / (R**2)

print "Attraction between Earth and Moon(meters):", attraction