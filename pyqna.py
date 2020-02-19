import csv
import os
from statistics import mean


file_path = os.path.join(".", "folder", "FL_insurance_sample.csv")
file_path_2 = "folder/FL_insurance_sample.csv"

output_file = "./output.txt"


with open(file_path_2, mode='r') as f:
    # reader = csv.DictReader(f)
    # to read a dictionary value dict['key'] will give you 'value'

    # to read a DictReader object row loop through reader and reference row['key']
    # for row in reader:
    #     print(row["policyID"])

    no_dict_reader = csv.reader(f)
    data_dict = {}
    for row in no_dict_reader:
        if row[0] not in data_dict.keys():
            data_dict[row[0]] = 1
            # for DictReader it would be data_dict['policyID'] = 1
        else:
            data_dict[row[0]] += 1
            # for DictReader: data_dict['policyID'] += 1

fake_csv_list = [2, 8, 6, 3, 10, 4, 5]


def write_twice(my_text, file_var):
    print(my_text)
    file_var.write(str(my_text) + '\n')


##################################
#           DONT DO THIS         #
##################################
# output = open(output_file, mode='w')
# UNLESS YOU DO THIS, BUT DONT DO THAT EITHER
# output.close()
with open(output_file, mode='w') as output:
    # output.write("This is my output file\n")
    write_twice("This is my output file", output)
    write_twice("These are my values", output)
    # print("stuff")
    for value in fake_csv_list:
        write_twice(value, output)
        # output.writelines([str(i)+"\n" for i in fake_csv_list])

    # output.write('text or anything else')

monthly_changes = []

for i in range(len(fake_csv_list)):
    if i != 0:
        monthly_changes.append(fake_csv_list[i] - fake_csv_list[i-1])

    # print(fake_csv_list.index(i))

avg_monthly_change = mean(monthly_changes)

# print(avg_monthly_change)


my_list = []
my_second_list = []
for i in range(9):
    my_list.append(i)

for i in range(1, 9):
    my_second_list.append(i)

zipped_list = zip(my_list, my_second_list)
# print([zipped for zipped in zipped_list])


# indexing

index_list = [1, 5, "seven", 4, 5]

# print(index_list[::-1])
# print(index_list)
# print(f"only the last: {index_list[-2]}")
# print("sort" + sorted(index_list, reverse=True))
# print(f'only some: {index_list[2:5]}')


# string concatenation:
my_string = "this is a string with spaces"
my_split = my_string.split(' ')
my_join = " ".join(my_split)
# print(my_join)


'''

{
    key: [0,1,2,3,4],
    "hobbies":['sports', 'board games', 'cooking'],
    "properties": {
        "id": 12345,
        "name": "John Smith",
        "occupation": "csv reader"
    },
    "candidate": list.append(row[0])
}
'''

append_dict = {}

append_dict['key1'] = ["list", "of", "strings"]

append_dict['key1'].append("another")

# print(append_dict)


# for i in range(10):
#     # print(f"i is {i}")
#     if i != 0:
#         # print(f"last row was {i-1}")
