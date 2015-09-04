#!/usr/bin/env python

import Orange
import shutil
import fileinput

shutil.copyfile("sample_data.tab", "__sample_data.tab")

# read frist line
lines = open("sample_data.tab").readline() 
old_line = lines[0:]

# create new first line
first_line = "	__".join([x[0:] for x in lines.split("	")]);
new_first_line =  "__" + first_line

# save new table with prefix "__"
for line in fileinput.input("__sample_data.tab", inplace=True): 
      print line.replace(old_line, new_first_line)

# create two different tables
data = Orange.data.Table("sample_data.tab")
data2 = Orange.data.Table("__sample_data.tab")

# table ready for prediction
new_table = Orange.data.Table([data, data2])
new_cleaned_table = Orange.data.Table(new_table.domain)


predict_list_domain = ["predict"]
predict_list = []

table = data.select(['user_id'])
table2 = data2.select(['__user_id'])

#index = 0
#index_2 = 0

non_orange_table = []

for index, inst in enumerate(table):
    selected_user_id = inst[0].native()
    for index_2, inst2 in enumerate(table2):
    	if selected_user_id == inst2[0].native():
    		predict_list.append('TAK')
    	else:
    		predict_list.append('NIE')
    	row = data[index].native(0) + data2[index_2].native(0)
    	non_orange_table.append(row)
    	pass

# print "end"
# result = non_orange_table + predict_list


# result_table = Orange.data.Table(new_cleaned_table.domain, non_orange_table)

print non_orange_table[3]
# print result_table.domain
# print result_table[0].native()
# print "dupa"
# # print result_table[2].native()
