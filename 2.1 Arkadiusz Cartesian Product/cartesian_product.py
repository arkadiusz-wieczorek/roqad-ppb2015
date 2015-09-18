#!/usr/bin/env python
import re
#from memory_profiler import profile

#@profile
def cartesianProduct(sample):
	x = ''.join(('__',sample[0]))

	first_part_domain = sample[0].replace("\n", "")
	second_part_domain = re.sub(r"\,([a-zA-Z])", ",__\\1", x)
	second_part_domain = second_part_domain.replace("\n", "")
	second_part_domain = second_part_domain.replace(" ", "")

	cartesian_product_domain = ""
	cartesian_product_domain = first_part_domain +','+ second_part_domain + ',' + 'the_same_user_id' + ',' + 'count_anonymous'

	del sample[0]
	i = cartesian_product_domain.split(',')
	
	index_of_anonymous_1 = [j for j, x in enumerate(i) if x == "anonymous_1"]
	index_of_second_anonymous_1 = [j for j, x in enumerate(i) if x == "__anonymous_1"]

	index_of_anonymous_1 = index_of_anonymous_1[0]
	index_of_second_anonymous_1 = index_of_second_anonymous_1[0]


	with open('result_cartesian.csv', "w") as file:
		file.write(cartesian_product_domain + '\n')
		for i in sample:
			# selected_user_id = i[0:i.find(',')]
			selected_user_id = i.split(',')[0]

			for j in sample:

				# if selected_user_id == j[0:j.find(',')]:
				if selected_user_id == j.split(',')[0]:
					predict = '1'
				else:
					predict = '0'
				row = i.replace("\n", "") + "," + j.replace("\n", "") + "," + predict
			
				list = row.split(',')
				
				count_anonymous = 0

				for x in range(70):
					index = index_of_anonymous_1 + x
					index_2 = index_of_second_anonymous_1 + x

					if list[index] == list[index_2] and list[index] != "X":
						count_anonymous = count_anonymous + 1
					pass
				pass
				row = row + "," + str(count_anonymous)
				file.write(row+'\n')
			pass
		pass
print 'results are saving in cartesian_product.csv'