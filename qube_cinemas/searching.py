
def read_file(file):
    import json 

    with open(text_file, 'r') as file1:
        data = json.load(file1)
    
    return data

def search_string(datas, string):

    for i in string:
        for key in datas:
            if key == i:    
                print("Searching for", i)
                print('     found in ')
                for value in datas[key]:
                    print('\t' + value)
                print()


from sys import argv

text_file = argv[1]

datas = read_file(text_file)

string_lyst = argv[2:]

search_string(datas, string_lyst)
