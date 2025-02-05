fp = open("text.txt", "r") # r is by default, so not really needed
print(fp.read()) #prints the entire content of the file
fp.close() # good practice to close the file

# same exact thing with context manager
with open("text.txt", "r") as fp:
    print(fp.read())

# lets read from the same file, line by line
with open("text.txt", "r") as fp:
    for line in fp: # we iterate over the file, line by line
        print(f"{line_number}:{line}", end="") # ask print not to add a new line
        # print(line.rstrip())
        line_number += 1
print("done printing")
