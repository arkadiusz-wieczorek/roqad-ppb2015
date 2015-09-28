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

		added = False
		for label in labels:

			if current_device_id in label:
				find_user_id = label[0:label.find(',')]

				dataset_with_added_user_id.append(find_user_id +','+row)
				added = True
		if(not(added)):
			print "NOt ADDED!"

	return dataset_with_added_user_id

# example execute
# addUserID('../roq-ad-data-set/learning-set/devices.csv', '../roq-ad-data-set/learning-set/labels.csv')
