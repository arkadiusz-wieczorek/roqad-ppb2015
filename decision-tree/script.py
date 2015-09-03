#!/usr/bin/env python

import Orange
import numpy
data = Orange.data.Table("sample_data.tab")
data2 = Orange.data.Table("2_sample_data.tab")


table = data.select(['user_id'])
table2 = data2.select(['2_user_id'])


# for inst in table:
#     selected_user_id = inst[0].native()
#     for inst2 in table2:
#     	if selected_user_id == inst2[0].native():
#     		print('TAK')
#     	else:
#     		print('NIE')


# predict_table = Orange.data.Domain[data.domain,data2.domain]
# predict_table = numpy.concatenate([data.domain, data2.domain])
# predict_table = Orange.data.Domain([data.domain, data2.domain])	
# print predict_table
# new_domain = Orange.data.Domain(printed_data_domain, data2.domain)

new_table = Orange.data.Table(data.domain, [])

new_table_2 = Orange.data.Table(data2.domain, new_table)
print new_table_2.domain