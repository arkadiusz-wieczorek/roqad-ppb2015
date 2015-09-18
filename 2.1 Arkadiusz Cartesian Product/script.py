#!/usr/bin/env python

import Orange
import shutil
import fileinput

print "start program"

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

# predict_domain = ["predict"]
predict_domain = Orange.data.Domain([Orange.feature.Discrete("predict")], False)
# print predict_domain.domain
predict_column = []

table = data.select(['user_id'])
table2 = data2.select(['__user_id'])

non_orange_table = []

for index, inst in enumerate(table):
    selected_user_id = inst[0].native()
    for index_2, inst2 in enumerate(table2):
    	if selected_user_id == inst2[0].native():
    		predict_column.append('TAK')
    	else:
    		predict_column.append('NIE')
    	row = data[index].native(0) + data2[index_2].native(0)
    	non_orange_table.append(row)
    	pass

# print non_orange_table

# print "table_without_predictions"
# table_without_predictions = Orange.data.Table(new_cleaned_table.domain, non_orange_table)

# print "table_of_predictions"
# table_of_predictions = Orange.data.Table(predict_domain, predict_column)

# print "result_table"
# result_table = Orange.data.Table([table_without_predictions, table_of_predictions])

# print result_table[2].native()