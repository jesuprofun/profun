
def dict_func(lyst):
    my_dict = dict()
    for i in lyst:
        my_dict[i] = i * i 
    print(my_dict) 

lyst = [x for x in range(10)]
dict_func(lyst)