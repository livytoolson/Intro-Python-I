"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""
# I/O = file input and output

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
# Best practice is to use context manager with the with keyword
open_file = open("foo.txt", "r")
print(open_file.read())
open_file.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
new_file = open("bar.txt", "a+") # a+ opens and creates a new file
new_file.write("Hello world!")
new_file.close()

new_file = open("bar.txt", "a") 
new_file.write("Welcome to CS Reset.")
new_file.close()

# r+ opens a file for reading and writing
# a appends - starts writing at the end 
# w will overwrite anything that is already in the file - starts writing on the first line