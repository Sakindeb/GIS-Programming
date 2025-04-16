# FOR LOOPS
coordinates = [
    (35.6895, 139.6917),
    (34.0522, -118.2437),
    (51.5074, -0.1278),
]  # List of tuples representing coordinates
for lat, lon in coordinates:
    print(f" Latitude: {lat} and Longitude: {lon}")

def calculate_distance(lat1, lon1, lat2, lon2):
    return ((lat2-lat1) ** 2 + (lon2 -lon1) ** 2) ** 0.5
reference = (0,0)
for lat, lon in coordinates:
    distance = calculate_distance(reference[0], reference[1], lat, lon)
    print(f" Distance is {distance} from reference point {reference}")
 # WHILE LOOPS
counter = 0
while counter < len(coordinates):
    lat, lon = coordinates[counter]
    print(f"Processing coordinate: ({lat}, {lon})")
    counter += 1

# Control statements allow you to execute different blocks of code based on certain conditions. In geospatial programming, this is useful for handling different types of data or conditions
for lat, lon in coordinates:
    if lat > 0:
        hemisphere = "Northern"
    else:
        hemisphere = "Southern"

    if lon > 0:
        direction = "Eastern"
    else:
        direction = "Western"

    print(
        f"The coordinate ({lat}, {lon}) is in the {hemisphere} Hemisphere and {direction} Hemisphere."
    )
# Combining
filtered_coordinates = []
for lat, lon in coordinates:
    if lon > 0:
        filtered_coordinates.append((lat, lon))
print(f"Filtered coordinates (only with positive longitude): {filtered_coordinates}")

southern_count = 0
for lat, lon in coordinates:
    if lat < 0:
        southern_count += 1
print(f"Number of coordinates in the Southern Hemisphere: {southern_count}")

# EXERCISE
city_coordinates = [
    ("Nairobi",35.6895, 139.6917),
    ("New Yourk",34.0522, -118.2437),
    ("Benin",51.5074, -0.1278),
] 

