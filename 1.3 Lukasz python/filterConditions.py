import roqatClasses
import csv

def requestBound(requestPerDevices, devices, bound):
	returnDevices = {}
	for key, device in devices.items():
		if len(requestPerDevices[key].request) > bound: 
			returnDevices[ key ] = requestPerDevices[key].device;
	return returnDevices
	
def labelBound(requestPerDevices, devices, bound):
	returnDevices = {}
	devicesUser = {}
	userDevices = {}
	with open('labels.csv') as csvfile:
		lables = csv.DictReader(csvfile, delimiter=",")
		for row in lables:
			if row['device_id'] in devicesUser:
				devicesUser[row['device_id']].addUser(row['user_id'])
			else:
				devicesUser[row['device_id']] = roqatClasses.DeviceUser(row['device_id'], [row['user_id']])
			if row['user_id'] in userDevices:
				userDevices[row['user_id']].addDevice(row['device_id'])
			else:
				userDevices[row['user_id']] = roqatClasses.UserDevice(row['user_id'], [row['device_id']])
#			print (row['user_id'] , ' ', len(userDevices[row['user_id']].devices))
#		for user in devicesUser[key].users:
#			if len(userDevices[user].devices) > bound: 
#				devices[key].update({'user_id' : devicesUser[key].users})


