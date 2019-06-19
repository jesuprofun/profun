

my_dict = {}
with open("Urban_Total_Accidents_2006-16.xls",'r') as file1:
    for line in file1:
        for i in range(0, len(line)):
            if line[i] == ',':
                my_dict[line[:i + 1]] = line[i+1 : len(line) - 1]
                # print(line[:i + 1])
                # print(line[i+1 : len(line) - 1])
                # lyst_keys.append(line[:i+1])
                # lyst_values.append(repr(line[i+1 : len(line) - 2]))
                break

print(my_dict)

# def convert_to_int(value):
#     try:
#         return int(value)
#     except ValueError:
#         return 0


# with open("Urban_Total_Accidents_2006-16.xls",'r') as csv_file:
#     states_dict = dict()
#     headers = csv_file.readline().strip().split(',')[1:]
#     for line in csv_file:
#         row_data = line.strip().split(',')
#         state = row_data[0]
#         row_data = [convert_to_int(value) for value in row_data[1:]]
#         states_dict[state] = {column_name: column_data for column_name, column_data in zip(headers, row_data)}
#         print(states_dict)
# # percentage_of_accidents_by_urban_population(states_dict)
# # percentage_of_accidents(states_dict)