# Object oriented programming (inheritance, dependency injection, abstraction)
# inheritance is being reinforced in this file - create a class and pass it's methods and variables to a new class
# read about the dunder __repr__  and dunder __str__ methods (dunder methods, protocal, magic methods)
# in terminal --> python3 --> dir(name of method) 

# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon: # base class
    def __init__(self, lat, lon):           # self is a reference to the object the method is being invoked on (lat, lon object), binds the attributes
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):                     # Waypoint is a child of LatLon
    def __init__(self, name, lat, lon):     # initializer
        self.name = name
        super().__init__(lat, lon)          # allows us to overwrite values of lat and lon
    def __str__(self):                      # returns the string representation of the object -- makes the object human readable, using this method when calling print method under the hood
        return f'name: {self.name}, lat: {self.lat}, lon: {self.lon}'

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):                   # Geocache is a grandchild of LatLon
    def __init__(self, name, difficulty, size, lat, lon):
        self.difficulty = difficulty
        self.size = size
        super().__init__(name, lat, lon)
    def __str__(self):
        return f"""         
        {self.name},
        diff {self.difficulty},
        size {self.size},            
        {self.lat},
        {self.lon}
        """
# triple quotes = docstring -- prints values on different lines
# useful to use docstrings for menu items
# /n (new line character) also prints values on new line

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
# creating a new instance of the class -->
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
# creating a new instance of the class -->
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)