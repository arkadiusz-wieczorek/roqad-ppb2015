#!/usr/bin/env python

import shutil
import fileinput

f=open('../mysql/ip_to_device.csv')
lines=f.readlines()
# print lines[26]
# print lines[30]

ip = lines[0]
last_seen_ip = ip[0:9]
# print last_seen_ip[0:9]

#ip,device_id
#
#

output = ""
count = -1;

for line in lines:
	current_ip = line[0:9]
	current_dev = line[10:20]
	# print current_ip
	if last_seen_ip == current_ip:
		if(count>=0):
			output += ","
		count+=1
	else:
		count = 0
		output += "\n"
		last_seen_ip = current_ip
	output += current_dev


print output
