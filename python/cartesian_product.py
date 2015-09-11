#!/usr/bin/env python
import re

def cartesianProduct(sample):
	x = ''.join(('__',sample[0]))

	first_part_domain = sample[0].replace("\n", "")
	second_part_domain = re.sub(r"\,([a-zA-Z])", ",__\\1", x)

	cartesian_product_domain = ""
	cartesian_product_domain = first_part_domain +','+ second_part_domain + ',' + 'prediction'

	cartesian_product = []
	cartesian_product.append(cartesian_product_domain)

	del sample[0]

	for i in sample:
		selected_user_id = i[0:i.find(',')]
		for j in sample:
			if selected_user_id == j[0:j.find(',')]:
				predict = '1'
			else:
				predict = '0'
			row = i.replace("\n", "") + "," + j.replace("\n", "") + "," + predict
			cartesian_product.append(row)
	return cartesian_product
	pass
