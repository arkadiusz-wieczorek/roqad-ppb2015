 #!/usr/bin/env python
import fileinput
import re

def addUserID(dataset_file, dataset_file_with_userID, mode):
	if mode == 1:
		dataset=open(dataset_file).readlines()
	else:
		dataset = dataset_file

	labels=open(dataset_file_with_userID).readlines()
	dataset_with_added_user_id = []

	for row in dataset:
		current_device_id = row[0:row.find(',')]

		found_any = False

		user_ids = []

		for label in labels:
			if current_device_id in label:
				found_any = True
				found_user_id = label[0:label.find(',')]
				user_ids.append(found_user_id)
		
		if(not(found_any)):
			print "NOt ADDED!"
		else:
			concatenated_user_ids= ";".join(user_ids)
			dataset_with_added_user_id.append(concatenated_user_ids +','+row)

	print "dataset_with_added_user_id length:", len(dataset_with_added_user_id)
	return dataset_with_added_user_id

# example execute
# addUserID('../roq-ad-data-set/learning-set/devices.csv', '../roq-ad-data-set/learning-set/labels.csv')
