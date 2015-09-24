#!/usr/bin/env python
import numpy
import fileinput
import re

devices_list = open("devices_list.csv").readlines()
indexes = len(devices_list)

matrix = numpy.zeros((indexes, indexes))

def devlistnum( dev_id ):
	for i in range(1,len(devices_list)-1):
		if devices_list[i].replace("\n", "") == dev_id:
			return i

devices_from_the_same_user = open("devices_from_the_same_user.csv").readlines()

# print devices_from_the_same_user[1].replace("\n", "").split(',')
# print devices_from_the_same_user[2].replace("\n", "").split(',')

for line in devices_from_the_same_user:
	arr = line.replace("\n", "").split(',')
	for i in range(len(arr)-1):
		
		for j in xrange(i+1,len(arr)):
			row = devlistnum(arr[i])
			column = devlistnum(arr[j])

			matrix[row][column] = 1
			matrix[column][row] = 1
			pass
		
		pass
matrix.tofile('output', sep=" ", format="%s")
print "matrix was written"
# with open('output', "w") as file:
# 	file.write(str(matrix) + '\n')