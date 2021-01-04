# For the exercise, look up the methods and functions that are available for use
# with Python lists.
# A list is like an array in JavaScript
# An array can only have one data type, a list can have multiple data types
# If you want to add to an array to have to create a new array twice the size of the one you have, a list memory management is different
# In order to use an array in python you have to use numpy

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
# .append = .push in JS
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.pop(4) # start from the beginning index of list
# x.pop(-3) # start from the last index of list
# x.remove(8) # takes up a lot of memory / time, not the most effective way. remove goes through every single item in the list looking for correct value
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
# x.insert(index, value)
x.insert(5, 99)
print(x)

# Print the length of list x
# YOUR CODE HERE
print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
# for number in x:
#     print(number*1000)
# list comprehension is similar to .map in JS --> 
new_list = [num*1000 for num in x]
print(new_list)

# convert numbers into string -->
# new_list = [str(num) for num in x]
# print(new_list)