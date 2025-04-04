# Variables and Data Types with GEO 
# Variable to hold number of point
number_of_points = 120
print(number_of_points)

# Data Types
# Integers
number_of_features = 500
# Float
latitude = 23.456
longitude = 14.6803
#Strings
coordinate_system = "WGS 84"
multiline_string= """"
something that is large
needs more lines
"""
#Booleans
is_georeferenced = False
#Lists
coordinates = [
    35.6895,
    139.6917,
] 
#Dictionaries
feature_attributes = {
    "name": "Mount Kenya",
    "height_meters": 5776,
    "type": "Volcanic",
    "location": [35.3606, 138.7274],
}

#Escape Characters
# \n introduces a new line
print("Hello World!\nThis is a Python script.")
# \t introduces a tab
print("This is the first line.\n\tThis is the second line. It is indented.")


# Basic Operations
number_of_features += 20
print("Updates number of features:", number_of_features)

#Conversion from degrees to radians
import math

latitude_radians = math.radians(latitude)
print("Latitude converted to radians from degrees:", latitude_radians)

#Adding new coordinates...Append
coordinates.append(12.093)
coordinates.append(11.89)
print("Updates coordinates:", coordinates)

#Accessing dictionary elements

mount_kenya_name= feature_attributes["name"]
mount_kenya_height= feature_attributes["height_meters"]

print(f"{mount_kenya_name} is {mount_kenya_height} meters high")

# Geospatial Context
# Example coordinates 
points = [
    [35.6895, 139.6917],  # Tokyo
    [34.0522, -118.2437],  # Los Angeles
    [51.5074, -0.1278],  # London
    [48.8566, 2.3522],  # Paris
]

#Calculate centroid
centroid_lat = sum([point[0] for point in points]) / len(points)
centroid_long = sum([point[1] for point in points]) /len(points)
centroid = [centroid_lat,centroid_long]

print("Centroid coordinates is:", centroid)


#List of tuples

kenya = (2.3443,2.345)
uganda = (1.344, 2.354)
tanzania = (1.76, 4.323)

centroid_latitude = (kenya[0]+ uganda[0]+ tanzania[0]) / 3
centroid_longitude = (kenya[1]+ uganda[1]+ tanzania[1]) /3

print(f"{centroid_latitude} latitude of centroid and {centroid_longitude} is the longitude of centroid")