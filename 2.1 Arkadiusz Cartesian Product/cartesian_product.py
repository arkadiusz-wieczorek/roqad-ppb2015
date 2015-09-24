#!/usr/bin/env python
import re
import url_dist as URLdist
import sys
import itertools

def filter_columns(values, original_columns, columns_to_remove):
	new_list = []
	for i in range(len(values)):
		should_add = True
		for column_regex in columns_to_remove:
			if(not(column_regex.match(original_columns[i]) is None)):
				should_add = False
		if (should_add):
			new_list.append(values[i])
	return new_list

def generate_map(column_names, values):
	data = zip(column_names, values)
	new_data = []
	for tup in data:
		new_data.append([tup[0], tup[1]])
	return dict(new_data)

def inter(a,b):
	c=[]
	for e in a:
		if e in b:
			c.append(e)
	return c

# ogleglosc miedzy urlami (z powtorzeniami)
def list_dist(a,b):
	x = len(inter(a,b))/float(min(len(a),len(b)))
	return x

def cartesianProduct(sample, device_url_path, output_file):
	once = 0
	x = ''.join(('__',sample[0]))

	first_part_domain = sample[0].replace("\n", "")


	second_part_domain = re.sub(r"\,([a-zA-Z])", ",__\\1", x)
	second_part_domain = second_part_domain.replace("\n", "")
	second_part_domain = second_part_domain.replace(" ", "")

	cartesian_product_domain = ""
	cartesian_product_domain = first_part_domain +','+ second_part_domain + ',' + 'the_same_user_id' + ',' + 'count_anonymous' + ',' + 'url_dist' + ',' + 'unique_url_dist,country_comp,same_browser_name,same_os_name,same_os_version,same_browser_version,same_device_name,same_device_category,comp_max_pages_per_hour,comp_med_pages_per_hour,comp_time,comp_dom_ips,comp_dom_providers,connection_comp'

	del sample[0]
	i = cartesian_product_domain.split(',')
	
	index_of_anonymous_1 = [j for j, x in enumerate(i) if x == "anonymous_1"]
	index_of_second_anonymous_1 = [j for j, x in enumerate(i) if x == "__anonymous_1"]

	index_of_anonymous_1 = index_of_anonymous_1[0]
	index_of_second_anonymous_1 = index_of_second_anonymous_1[0]

	URLdist.loadDataset(device_url_path)

	count = 0;

	columns_to_remove = ["(__)?anonymous.*", "(__)?user_id", "(__)?device_id", "(__)?Country.*", "(__)?browser_name", "(__)?os_name", "(__)?os_version", "(__)?browser_version", "(__)?device_name", "(__)?category", "(__)?PageMax", "(__)?PageMed", "(__)?Czas.*", "(__)?IP[0-9]+", "(__)?ISP[0-9]+", "(__)?Start.*", "(__)?Conn.*"]
	columns_to_remove = map(re.compile, columns_to_remove)

	single_row_domain = first_part_domain.split(",")

	original_domain = cartesian_product_domain.split(",")

	new_domain = ",".join(filter_columns(original_domain, original_domain, columns_to_remove))

	with open(output_file, "w") as file:
		file.write(new_domain + '\n')
		for i in sample:

			row = []

			selected_user_id = i.split(',')[0]

			device1_row = i[:-1].split(",")
			device1_filtered_row = filter_columns(device1_row, original_domain, columns_to_remove)
			device1 = generate_map(single_row_domain, device1_row)


			for j in sample:

				row = []
				row.extend(device1_filtered_row)

				device2_row = j[:-1].split(",")
				device2_filtered_row = filter_columns(device2_row, original_domain, columns_to_remove)
				device2 = generate_map(single_row_domain, device2_row)

				row.extend(device2_filtered_row)

				if(device1["device_id"]==device2["device_id"]):
					continue

				#check if the 2 devices are for the same user ("the_same_user_id" column. 1 for true, 0 for false)

				the_same_user_id = 1 if device1["user_id"]==device2["user_id"] else 0
			
				row.append(the_same_user_id)

				#compare anonymous values ("count_anonymous" column. Values from 0 to 70)

				count_anonymous = 0

				for x in range(1, 71):
					attr_name ="anonymous_" + str(x) 
					if((device1[attr_name]!="") & (device2[attr_name]!="")):
						if(device1[attr_name] == device2[attr_name]):
							count_anonymous = count_anonymous + 1
				row.append(count_anonymous)

				#url_dist and unique_url_dist

				url_dist = URLdist.dist(device1["device_id"], device2["device_id"]);
				unique_url_dist = URLdist.distunique(device1["device_id"], device2["device_id"]);
				row.extend([url_dist, unique_url_dist]);



				#compare countries ("country_comp" column. Values from 0 to 1)
				for column_name in ["CountryDom", "CountryDom2", "CountryCount"]:
					device1[column_name] = int(device1[column_name])
					device2[column_name] = int(device2[column_name])
				same_country_dom_1 = 0.5 if device1["CountryDom"]==device1["CountryDom"] else 0
				same_country_dom_2 = 0.2 if device1["CountryDom2"]==device1["CountryDom2"] else 0
				compare_country_counts = min([device1["CountryCount"], device2["CountryCount"]])/max([device1["CountryCount"], device2["CountryCount"]]) * 0.2

				country_comp = same_country_dom_1 + same_country_dom_2 + compare_country_counts
				row.append(country_comp)

				#compare browser names ("same_browser_name" column. 1 for true, 0 for false)
				same_browser_name = 1 if device1["browser_name"]==device1["browser_name"] else 0
				row.append(same_browser_name)

				#compare os names ("same_os_name" column. 1 for true, 0 for false)
				same_os_name = 1 if device1["os_name"]==device1["os_name"] else 0
				row.append(same_os_name)

				#compare os version ("same_os_version" 1 for true, 0 for false)
				same_os_version = 0
				if((device1["os_version"]!="") & (device2["os_version"]!="")):
					if(device1["os_version"]==device2["os_version"]):
						same_os_version = 1
				row.append(same_os_version)

				#compare browser version ("same_browser_version" 1 for true, 0 for false)
				same_browser_version = 0
				if((device1["browser_version"]!="") & (device2["browser_version"]!="")):
					if(device1["browser_version"]==device2["browser_version"]):
						same_browser_version = 1
				row.append(same_browser_version)


				#compare device name ("same_device_name", 1 for true, 0 for false)
				same_device_name = 1 if device1["device_name"]==device2["device_name"] else 0
				row.append(same_device_name)

				#compare category ("same_device_category", 1 for true, 0 for false)
				same_device_category = 1 if device1["category"]==device2["category"] else 0
				row.append(same_device_category)

				#compare max_pages_per_hour ("comp_max_pages_per_hour", 1 for very similar, 0 for very dissimilar)
				M = max(map(int, [device1["PageMax"], device2["PageMax"]]))
				m = min(map(int, [device1["PageMax"], device2["PageMax"]]))
				comp_max_pages_per_hour = float(1)/(float(1 + M -m)**2)
				row.append(comp_max_pages_per_hour)

				#compare med_pages_per_hour ("comp_med_pages_per_hour", 1 for very similar, 0 for very dissimilar)
				M = max(map(int, [device1["PageMed"], device2["PageMed"]]))
				m = min(map(int, [device1["PageMed"], device2["PageMed"]]))
				comp_med_pages_per_hour = float(1)/(float(1 + M -m)**2)
				row.append(comp_med_pages_per_hour)

				#compare time of the requests ("comp_time", values from 0 to 1)
				common_ones = 0;
				total_dev1 = 0
				total_dev2 = 0
				for t in range(24):
					attr_name = "Czas" + str(t)
					if((device1[attr_name]==device2[attr_name]) & (str(device1[attr_name])=="1")):
						common_ones = common_ones + 1
					if(str(device1[attr_name])=="1"):
						total_dev1 = total_dev1 + 1
					if(str(device2[attr_name])=="1"):
						total_dev2 = total_dev2 + 1

				max_in_dev = float(max([total_dev1, total_dev2]));

				if(max_in_dev>0):
					comp_time = float(common_ones)/max_in_dev
				else:
					comp_time = 0
				row.append(comp_time)

				#compare dominant IPs ("comp_dom_ips", from 0 to 1)
				ips_1 = []
				ips_2 = []
				for t in range(24):
					attr_name = "IP" + str(t)
					if((device1[attr_name]!="")  & (str(device1[attr_name])!="0")):
						ips_1.append(device1[attr_name])
					if((device2[attr_name]!="")  & (str(device2[attr_name])!="0")):
						ips_2.append(device2[attr_name])
				ips_1_unique = []
				ips_2_unique = []
				for el in set(ips_1):
					ips_1_unique.append(el)
				for el in set(ips_2):
					ips_2_unique.append(el)

				comp_dom_ips = list_dist(ips_1_unique, ips_2_unique)
				row.append(comp_dom_ips)

				#compare dominant providers ("comp_dom_providers", from 0 to 1)
				providers_1 = []
				providers_2 = []
				for t in range(24):
					attr_name = "ISP" + str(t)
					if((device1[attr_name]!="")  & (str(device1[attr_name])!="0")):
						providers_1.append(device1[attr_name])
					if((device2[attr_name]!="")  & (str(device2[attr_name])!="0")):
						providers_2.append(device2[attr_name])
				providers_1_unique = []
				providers_2_unique = []
				for el in set(providers_1):
					providers_1_unique.append(el)
				for el in set(providers_2):
					providers_2_unique.append(el)

				comp_dom_providers = list_dist(providers_1_unique, providers_2_unique)
				row.append(comp_dom_providers)


				# removed because of insufficient data
				# #compare startPageMax ("comp_max_start_pages_per_hour", 1 for very similar, 0 for very dissimilar)
				# M = max(map(int, [device1["StartPageMax"], device2["StartPageMax"]]))
				# m = min(map(int, [device1["StartPageMax"], device2["StartPageMax"]]))
				# if(int(device1["StartDays"])>=10 & int(device2["StartDays"])>=10):
				# 	comp_max_start_pages_per_hour = float(1)/(float(1 + M -m)**2)
				# else:
				# 	comp_max_start_pages_per_hour = "x"
				# row.append(comp_max_start_pages_per_hour)

				# #compare med_pages_per_hour ("comp_med_pages_per_hour", 1 for very similar, 0 for very dissimilar)
				# M = max(map(int, [device1["StartPageMed"], device2["StartPageMed"]]))
				# m = min(map(int, [device1["StartPageMed"], device2["StartPageMed"]]))
				# if(int(device1["StartDays"])>=10 & int(device2["StartDays"])>=10):
				# 	comp_med_start_pages_per_hour = float(1)/(float(1 + M -m)**2)
				# else:
				# 	comp_med_start_pages_per_hour = "x"
				# row.append(comp_med_start_pages_per_hour)

				#compare connection_type ("connection_comp" column. Values from 0 to 1)
				for column_name in ["ConnDom", "ConnDom2", "ConnDiff"]:
					device1[column_name] = int(device1[column_name])
					device2[column_name] = int(device2[column_name])
				same_Conn_dom_1 = 0.5 if device1["ConnDom"]==device1["ConnDom"] else 0
				same_Conn_dom_2 = 0.2 if device1["ConnDom2"]==device1["ConnDom2"] else 0
				if(max([device1["ConnDiff"], device2["ConnDiff"]])==0):
					compare_Conn_counts = 0
				else:
					compare_Conn_counts = min([device1["ConnDiff"], device2["ConnDiff"]])/max([device1["ConnDiff"], device2["ConnDiff"]]) * 0.2

				connection_comp = same_Conn_dom_1 + same_Conn_dom_2 + compare_Conn_counts
				row.append(connection_comp)

				row = map(str, row)
				file.write(",".join(row)+'\n')
			pass
			count= count + 1
			print count/float(len(sample)) * 100,  "%"
		pass
print 'results are saving in cartesian_product.csv'