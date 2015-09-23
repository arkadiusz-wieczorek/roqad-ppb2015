import csv

def readFiles(devicesFile, requestFile):
	devicesReturn = {}
	requestReturn = {}
	with open(devicesFile) as csvfile:
		devices = csv.DictReader(csvfile, delimiter=",")
		for row in devices:
			devicesReturn[row['device_id']] = row
	with open(requestFile) as csvfile:
		request = csv.DictReader(csvfile, delimiter=",")
		index = 0 
		for row in request:
			requestReturn[index] = row
			index += 1
	return devicesReturn, requestReturn