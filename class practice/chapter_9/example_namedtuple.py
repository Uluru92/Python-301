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

# Modifying the tuple to a dic
null_island_dict = null_island._asdict()
null_island_dict["name"] = "Null Island is not an island"

modified_null_island = Geolocation(**null_island_dict)
print(modified_null_island)  # Geolocation(name='Null Island is not an island', lat=0, lon=0)


# Another Geolocation.. this time Maccu Piccu
maccu_piccu = Geolocation(name="Maccu Piccu", lat=-13.163108055193145, lon=-72.54496539348477)
maccu_piccu_tuple = ("Maccu Piccu", -13.163108055193145, 72.54496539348477)

# Get the latitude from the plain tuple
print(maccu_piccu_tuple[1])  # -13.163108055193145 - Wait... or was it at index 0? Or index 2? Arrgh!

# Get the latitude from the namedtuple
print(maccu_piccu.lat)  # -13.163108055193145 - Yay!

# Automatically generated docstrings
print("null_island docstring:")
print(null_island.__doc__)
print("\nnull_island_dict docstring: ")
print(null_island_dict.__doc__)
print("\nmaccu_piccu_tuple docstring: ")
print(maccu_piccu_tuple.__doc__)