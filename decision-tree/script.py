#!/usr/bin/env python

import Orange
data = Orange.data.Table("sample_data.tab")
# data2 = Orange.data.Table("sample_data.tab")
# data2 = data.select(data.domain)

data2 = Orange.data.Table(data)
data2.domain = Orange.data.Domain(data.domain)


for inst in data2.domain:
	data2.domain[inst].name = '__' + data2.domain[inst].name

print data.domain
print data2.domain

table = data.select(['user_id'])
table2 = data2.select(['__user_id'])

new_table = Orange.data.Table([data, data2])
print len(new_table)

new_cleaned_table = Orange.data.Table(new_table.domain)
print new_cleaned_table.domain

predict_list = []

for inst in table:
    selected_user_id = inst[0].native()
    for inst2 in table2:
    	if selected_user_id == inst2[0].native():
    		predict_list.append('TAK')
    	else:
    		predict_list.append('NIE')