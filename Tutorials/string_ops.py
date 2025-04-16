# Creating and Manipulating Strings
location_name = "Mount Everest"
location_name_full = location_name + ", Nepal"
print(location_name_full)

# Repeat with *
separator = "-" * 10
print(separator)

#SQL QUERY
table_name = "locations"
condition = "country = 'Nepal'"
sql_query = f"SELECT * FROM {table_name} WHERE {condition};"
print(sql_query)

#String Methods for Geospatial Data
# lower(), upper(): Convert strings to lowercase or uppercase.
location_name_upper = location_name.upper()
print(location_name_upper)  # Convert to uppercase
# strip(): Remove leading and trailing whitespace.
location_name_clean = location_name.strip()
print(location_name_clean)
# lstrip(), rstrip(): Remove leading or trailing whitespace.

# replace(): Replace a substring with another substring.
location_name_replaced = location_name.replace("Everest", "K2")
print(location_name_replaced)
# split(): Split a string into a list of substrings based on a delimiter.
location_parts = location_name_full.split(", ")
print(location_parts)
# join(): Join a list of strings into a single string with a specified delimiter.
countries = [" nepal", "INDIA ", "china ", "Bhutan"]
normalized_countries = [country.strip().title() for country in countries]
print(normalized_countries)
# Fornat
latitude = 27.9881
longitude = 86.9250
formatted_coordinates = "Coordinates: ({}, {})".format(latitude, longitude)
print(formatted_coordinates)

wkt_point = f"POINT({longitude} {latitude})"
print(wkt_point)

# Parsing
coordinate_string = "27.9881N, 86.9250E"
lat_str, lon_str = coordinate_string.split(", ")
latitude = float(lat_str[:-1])  # Convert string to float and remove the 'N'
longitude = float(lon_str[:-1])  # Convert string to float and remove the 'E'
print(f"Parsed coordinates: ({latitude}, {longitude})")

address = "123 Everest Rd, Kathmandu, Nepal"
street, city, country = address.split(", ")
print(f"Street: {street}, City: {city}, Country: {country}")

# Exercise
city = "Nairobi"
city_lower = city.lower()
city_upper = city.upper()
print(city_lower)
coordinates_ex = "40.7128N, 74.0060W"
lat_ex, long_ex = coordinates_ex.split(",")
lat_ex= lat_ex[:-1]
long_ex = long_ex[:-1]
name_loc = "The coordinates of: {} are: {}, {}".format(city, lat_ex, long_ex)
name_loc_form= f" The coordinates of {city} is {lat_ex}, {long_ex}"
print(name_loc)
print(name_loc_form)
another_city = "San Diego"
another_city = another_city.replace(" Diego", " Fransico")
print(another_city)
addresses = "Ruaka, Nairobi, Kenya"
street, city_c, country_n = addresses.split(",")
add_dict = {
    "street" : street,
    "city": city_c,
    "county": country_n,

}
print(add_dict)
