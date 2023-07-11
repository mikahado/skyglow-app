from skyfield.api import load
from skyfield.api import N, W, wgs84
# from skyfield.positionlib import Apparent

# Creates a timescale and ask the current time.
ts = load.timescale()
t = ts.now()

# Loads the JPL ephemeris DE421
planets = load('de421.bsp')
earth, sun = planets['earth'], planets['sun']

nyc = earth + wgs84.latlon(40.7128 * N, 74.0060 * W, elevation_m=10.0)

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

print("Observer data relative to Sun:", astrometric)
print("Sun's Altitude from Observer:", altitude)
print("Sun's Azimuth from Observer:", azimuth)
print("Sun's Degree from Observer:", degree)

if is_sunlit:
    print("The sun is up in NYC.")
else:
    print("The sun is down in NYC.")

print("The sun is in the", cardinal_direction, "direction.")

print("The direction of the sun relative to North is:", round(sun_direction),"deg.")
