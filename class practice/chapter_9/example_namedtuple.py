from collections import namedtuple

Geolocation = namedtuple("Geolocation", "name lat lon")

null_island = Geolocation(name="Null Island", lat=0, lon=0)

# Using zero-based indexing
print(null_island[0])  # "Null Island"
print(null_island[1])  # "0"
print(null_island[2])  # "0"

# Using dot notation
print(null_island.name)  # "Null Island"

# Using ._fields
print(null_island._fields)  # "('name', 'lat', 'lon')"
print(null_island._fields[0])  # "('name', 'lat', 'lon')"
print(null_island._fields[1])  # "'lat'
print(null_island._fields[2])  # "'lon'

# Using ._asdict
print(null_island._asdict())  # "{'name': 'Null Island', 'lat': 0, 'lon': 0}"
print(null_island._asdict()["name"]) # "Null Island"
print(null_island._asdict()["lat"])  # "0"
print(null_island._asdict()["lon"])  # "0"

