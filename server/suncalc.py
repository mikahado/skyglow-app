from skyfield.api import load
from skyfield.api import N, W, wgs84

# Create a timescale and ask the current time.
ts = load.timescale()
t = ts.now()

# Load the JPL ephemeris DE421 (covers 1900-2050).
planets = load('de421.bsp')
earth, sun = planets['earth'], planets['sun']

# position of Sun, viewed from Earth?
astrometric = earth.at(t).observe(sun)
ra, dec, distance = astrometric.radec()

print(ra)
print(dec)
print(distance)

boston = earth + wgs84.latlon(40.7128 * N, 74.0060 * W)
astrometric = boston.at(t).observe(sun)
alt, az, d = astrometric.apparent().altaz()

print(alt)
print(az)