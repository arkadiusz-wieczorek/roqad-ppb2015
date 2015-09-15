#!/usr/bin/env python
import re

def cartesianProduct(sample):
	x = ''.join(('__',sample[0]))

	first_part_domain = sample[0].replace("\n", "")
	second_part_domain = re.sub(r"\,([a-zA-Z])", ",__\\1", x)

	cartesian_product_domain = ""
	cartesian_product_domain = first_part_domain +','+ second_part_domain + ',' + 'the_same_user_id' + ',' + 'count_anonymous'

	del sample[0]
	i = cartesian_product_domain.split(',')
	
	index_of_anonymous_1 = [j for j, x in enumerate(i) if x == "anonymous_1"]
	index_of_second_anonymous_1 = [j for j, x in enumerate(i) if x == "__anonymous_1"]

	index_of_anonymous_1 = index_of_anonymous_1[0]
	index_of_second_anonymous_1 = index_of_second_anonymous_1[0]

	index_i = 0

	with open('cartesian_product.csv', "w") as file:
		for i in sample:
			selected_user_id = i[0:i.find(',')]

			index_j = 0

			for j in sample:

				if selected_user_id == j[0:j.find(',')]:
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


				index_j= index_j + 1
				print (len(sample) * index_i + index_j)/(len(sample)*len(sample))
			pass

			index_i = index_i + 1
				
		pass

	with open('cartesian_product.csv', 'r+') as file:
		content = file.read()
		file.seek(0, 0)
		file.write(cartesian_product_domain + '\n' + content)
print 'results saved in cartesian_product.csv'