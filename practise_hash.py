listFiles=["new_1.txt", "new_2.txt"]


for file in listFiles:
    with open(file, 'r') as file1:
        lines = file1.read().strip().split()

    lyst = []

    filedata = {}
    for word in lines:
        if word not in lyst:
            filedata[word] = []

        lyst.append(word)
    
        count = 1

    for key, value in filedata.items():
        value.append(listFiles[0])
        value.append(count)

        print(key)
        for k in value:
            print(k, value[k])