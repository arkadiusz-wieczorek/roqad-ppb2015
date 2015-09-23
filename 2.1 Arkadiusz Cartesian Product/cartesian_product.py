#!/usr/bin/env python
import re
import url_dist as URLdist
import sys


def cartesianProduct(sample, device_url_path, output_file):
	once = 0
	x = ''.join(('__',sample[0]))

	first_part_domain = sample[0].replace("\n", "")
	second_part_domain = re.sub(r"\,([a-zA-Z])", ",__\\1", x)
	second_part_domain = second_part_domain.replace("\n", "")
	second_part_domain = second_part_domain.replace(" ", "")

	cartesian_product_domain = ""
	cartesian_product_domain = first_part_domain +','+ second_part_domain + ',' + 'the_same_user_id' + ',' + 'count_anonymous' + ',' + 'url_dist' + ',' + 'unique_url_dist'

	del sample[0]
	i = cartesian_product_domain.split(',')
	
	index_of_anonymous_1 = [j for j, x in enumerate(i) if x == "anonymous_1"]
	index_of_second_anonymous_1 = [j for j, x in enumerate(i) if x == "__anonymous_1"]

	index_of_anonymous_1 = index_of_anonymous_1[0]
	index_of_second_anonymous_1 = index_of_second_anonymous_1[0]

	URLdist.loadDataset(device_url_path)

	count = 0;

	with open(output_file, "w") as file:
		file.write(cartesian_product_domain + '\n')
		for i in sample:

			selected_user_id = i.split(',')[0]


			for j in sample:

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

				devices = [s for s in list if 'dev_' in s]
				if((devices[0] is not None) & (devices[1] is not None)):
					url_dist = URLdist.dist(devices[0], devices[1])

					unique_url_dist = URLdist.distunique(devices[0], devices[1])
				
					row = row + "," + str(count_anonymous) + "," + str(url_dist) + "," + str(unique_url_dist)

				file.write(row+'\n')
			pass
			count= count + 1
			print count/float(len(sample)) * 100,  "%"
		pass
print 'results are saving in cartesian_product.csv'