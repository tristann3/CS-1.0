
#this will read all the lines of the file and return a list of line strings
def get_file_lines(filename):
    return open(filename, "r").readlines()

# this will loop through my list reversed, print the current length of the list along with the line string
# then it will remove the last element to keep the line number accurate
def lines_printed_backwards(lines_list):
    for line in reversed(lines_list):
        print(f"{len(lines_list)} {line}")
        lines_list.pop()
    return

file = "poem.txt"
file_lines = get_file_lines(file)

lines_printed_backwards(file_lines)
