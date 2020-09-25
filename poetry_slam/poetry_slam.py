

def get_file_lines(filename):
    return open(filename, "r").readlines()

 #print lines in reverse and include line numbers
def print_lines_backwards(lines_list):
    return

file = "poem.txt"
file_lines = get_file_lines(file)
for line in file_lines:
    print(line)

