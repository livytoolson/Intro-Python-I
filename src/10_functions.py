# Write a function is_even that will return true if the passed-in number is even.
# Don't use python to write JavaScript!
from dis import dis # debugging tool

# YOUR CODE HERE
def is_even(num):
    return num%2 == 0 # shorthand way

    # if num%2 == 0:
    #     return True # always capitalize boolean! 
    # return False

print(is_even(8))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def print_even(val):
    if num % 2 == 0:
        print("Even!")
    else:
        print("Odd!")

print(print_even(17))

dis(print_even)

# Python does one pass and executes one line at a time from top to bottom