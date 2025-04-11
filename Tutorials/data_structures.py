# Tuples, lists, sets and dicts enable efficient storage, management and manipulation of various types of data.
# Understand the characteristics and use cases of Python tuples, lists, sets, and dictionaries.
# Apply these data structures to store and manipulate geospatial data, such as coordinates, paths, and attribute information.
# Differentiate between mutable and immutable data structures and choose the appropriate structure for different geospatial tasks.
# Perform common operations on these data structures, including indexing, slicing, adding/removing elements, and updating values.
# Utilize dictionaries to manage geospatial feature attributes and understand the importance of key-value pairs in geospatial data management.


# TUPLES: IMMUTABLE SEQUENCES. Storing fixed collections of items
point = (
    35.6895,
    139.6917,
)  # Tuple representing a geographic point (latitude, longitude)

latitude =point[0]
longitude = point[1]

print(f" The place coordinates are latitude: {latitude} and longitude: {longitude}")

# LISTS: ordered, mutable sequences, meaning you can change, add, or remove elements after the list has been created. Lists are very flexible and can store multiple types of data, making them useful for various geospatial tasks

polygon_points = [
    (2.34,5.645),
    (3.578, 2.68),
    (2.12, 4.56),
]# Representing points enclosing a polygon

#ADD NEW POINT= APPEND
polygon_points.append((2.45, 67.34))
print("Updated polygon:", polygon_points)

#Slicing is accessing a subset
sub_polygon_points = polygon_points[:2]
print(sub_polygon_points)


# SETS unordered collections of unique elements. Sets are useful when you need to store a collection of items but want to eliminate duplicates.
regions = ["North America", "South America", "Asia"]
regions = set(regions)

regions.add("Africa")
print("Updates regions:", regions)

# DICTIONARIES
city_attributes ={
    "name": "Nairobi",
    "population": 239003400,
    "coordinates": (23.7624, 23.657),
}

city_name = city_attributes["name"]
city_populace = city_attributes["population"]
print(f"City name is: {city_name} and its populace is: {city_populace}")

city_attributes["Area_km2"] = "32890"
print("Updated city attributes:", city_attributes)


# EXERCISE
mt_attribute = {
    "name": "Mt Kenya",
    "height" : 2343400340,
    "location": "Central Kenya",
}

mt_attribute["snow"] = True
print("These are the attributes of Mt Kenya:", mt_attribute)
