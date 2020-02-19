import csv
import os
from statistics import mean

file_path = os.path.join(".", "folder", "FL_insurance_sample.csv")


with open(file_path) as f:
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
monthly_changes = []
fake_csv_list = [2, 8, 6, 3, 10, 4, 5]

for i in range(len(fake_csv_list)):
    if i != 0:
        monthly_changes.append(fake_csv_list[i] - fake_csv_list[i-1])

    # print(fake_csv_list.index(i))

avg_monthly_change = mean(monthly_changes)

print(avg_monthly_change)


my_list = []
my_second_list = []
for i in range(9):
    my_list.append(i)

for i in range(1, 9):
    my_second_list.append(i)

zipped_list = zip(my_list, my_second_list)
# print([zipped for zipped in zipped_list])


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
