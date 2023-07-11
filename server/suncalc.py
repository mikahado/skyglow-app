from skyfield.api import load
from skyfield.api import N, W, wgs84
from skyfield.positionlib import Apparent

# Create a timescale and ask the current time.
ts = load.timescale()
t = ts.now()

# Load the JPL ephemeris DE421 (covers 1900-2050).
planets = load('de421.bsp')
earth, sun = planets['earth'], planets['sun']

nyc = earth + wgs84.latlon(40.7128 * N, 74.0060 * W, elevation_m=10.0)

# position of Sun, viewed from Earth?
# astrometric = earth.at(t).observe(sun)

astrometric = nyc.at(t).observe(sun)

apparent = astrometric.apparent()
altitude, azimuth, degree = astrometric.apparent().altaz()

is_sunlit = altitude.degrees > 0
sun_direction = azimuth.degrees

direction_mapping = {
    (0, 22.5): 'N',
    (22.5, 67.5): 'NE',
    (67.5, 112.5): 'E',
    (112.5, 157.5): 'SE',
    (157.5, 202.5): 'S',
    (202.5, 247.5): 'SW',
    (247.5, 292.5): 'W',
    (292.5, 337.5): 'NW',
    (337.5, 360): 'N'
}

cardinal_direction = ''
for degree_range, direction in direction_mapping.items():
    if degree_range[0] <= sun_direction < degree_range[1]:
        cardinal_direction = direction
        break

print("NYC DATA STRCUTURE:", nyc)
print("astrometric", astrometric)
print("altitude:", altitude)
print("azimuth:", azimuth)
print("degree:", degree)

if is_sunlit:
    print("NYC is sunlit.")
else:
    print("NYC is not sunlit.")

print("The direction of the Sun relative to north is:", sun_direction, "degrees.")
print("The Sun is in the", cardinal_direction, "direction relative to north.")

print("Azimuth:", azimuth.degrees)