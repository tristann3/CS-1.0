import random

# this will read all the lines of the file and return a list of line strings
def get_file_lines(filename):
    return open(filename, "r").readlines()

# this will loop through my list reversed, print the current length of the list along with the line string
# then it will decrease the line counter
def lines_printed_backwards(lines_list):
    total_lines = len(lines_list)
    for line in reversed(lines_list):
        print(f"{total_lines} {line}")
        total_lines -= 1

# this will loop through my list randomly
def lines_printed_random(lines_list):
    total_lines = len(lines_list) - 1 #since indexing starts at zero, we must decrease the total linesfor out of bounds errors
    for line in lines_list:
        rand_line = random.randint(1,total_lines)
        print(lines_list[rand_line])

# this will print my list in a first-last pattern so it will print line 1, then 18, 2, 17 and so on...until it reaches the end of the poem
def lines_printed_custom(lines_list):
    nl = '\n'
    for x in range(int(len(lines_list)/2)): # this is the length of the list divided by two because we are printing 2 lines per iteration
        print(f"{x+1} {lines_list[x]}")
        print(f"{len(lines_list) - x} {lines_list[len(lines_list) - x - 1]} {nl}") # by referencing the index of the length of the list minus the current iteration minus 1, we can access the bottom of the poem recursively(?)


file = "poem.txt"
file_lines = get_file_lines(file)

#lines_printed_backwards(file_lines)

#lines_printed_random(file_lines)

lines_printed_custom(file_lines)
