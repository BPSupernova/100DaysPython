file = open("Day24/test_file.txt")
contents = file.read()
print(contents)
file.close() # Removable upon replacing line 1 with with open() as variable_name:

with open("new_file.txt", mode = "w") as file: # Creates the file if not already in the directory and writes the text into it
    file.write("New text!")
    