"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

# Two ways to make an empty dictionary -->
# dictionary = {}
# dictionaryTwo = dict()
# Don't use dict as a variable name because it is a built in function and you don't want to overwrite something

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE
new_waypoint = {
    "lat": 40,
    "lon": -20,
    "name": "last place"
}

waypoints.append(new_waypoint)
print(waypoints)

# waypoints.append({
#     "lat": 40,
#     "lon": -20,
#     "name": "last place"
# })


# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE
# this method replaces entire dictionary -->
# waypoints[0] = {
#     "lat": 43,
#     "lon": -130,
#     "name": "not a real place"
# }

# .update() allows you to pick exactly what keys you want to change
waypoints[0].update(name = "not a real place", lon = -130)
print(waypoints)

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
for values in waypoints:
    print(values["lat"], values["lon"])