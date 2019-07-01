
def file_open():
    with open("process.txt", 'r') as file1:
        lines = file1.readlines()

    return lines

def parsing_lines(lines):
    lyst = []
    for line in lines:
        lyst.append(line.strip().split())
    print(lyst[2])



lines = file_open() 
parsing_lines(lines)