# Write a python program to print the contents of a directory using the os module. Search online for the function which does that.
# Problem 5: Label the program written in problem 4 with comments.

import os

# Specify the directory you want to list
directory_path = '/'    # your directory/path #

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)

# print(contents)  #this also works