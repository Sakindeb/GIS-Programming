# EXERCISE ONE Variable Assignment and Basic Operations

coordinates = (40.7128, -74.0060)
latitude = coordinates[0]
longitude = coordinates[1]

population = 8336817
area_km2 = 783.8

population_density = population / area_km2
print(f" Lattitude: {latitude}, Longitude: {longitude}")

# Exercise 2: Working with Strings

city = "San Francisco"

# Exercise 3: Using Lists

cities = [
   ("New Youk City: (40.7128, -74.0060"),
   ("Los Angeles: (34.0522, -118.2437)"),
   ("Chicago: (41.8781, -87.6298)"),
]

cities.append("Miami: (25.7617, -80.1918)")

print(cities)
print(cities[:2])

# Exercise 4: Using Tuples
eiffel_tower = (48.8584, 2.2945)
print(eiffel_tower[0])
print(eiffel_tower[1])

# Exercise 5: Working with Sets
countries = ["USA", "FRANCE", "GERMANY"]
countries =set(countries)

countries.add("Kenya")
countries.add("USA")
print(countries)

#Exercise 6: Working with Dictionaries
river_attributes = {
    "Name": "Amazon River",
    "Length": 6400,
    "Countries": ["Brazil", "Peru", "Colombia"],
}

river_attributes["dischargem3/s"] = 209000
river_attributes["Length"] = 6992
print(river_attributes)