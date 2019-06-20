
def read_file(file):

    with open(text_file, 'r') as file1:
        lines = file1.readlines()
    
    return lines

def search_string(lines, strings):

    mylines = []
    for line in lines:
        mylines.append(line.strip('\n'))
    for element in mylines:
        print(element)
        
    print(mylines[4])



from sys import argv

script, text_file, strings = argv

lines = read_file(text_file)

ans = search_string(lines, strings)
print(ans)

