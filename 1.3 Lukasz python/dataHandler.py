import roqatClasses
import filterConditions
import datetime

def joinRequestDevices(devices, request):
	returnDevicesRequestMap = {}
	for key, device in devices.items():
		returnDevicesRequestMap[key] = roqatClasses.DevicesRequest(device, [])
	for key, request in request.items():
		if request['device_id'] in returnDevicesRequestMap:
			request.update({'czas' : datetime.datetime.fromtimestamp(int(request['timestamp'])/ 1e3).strftime('%Y-%m-%d %H:%M:%S')})
			returnDevicesRequestMap[ request['device_id'] ].addRequest(request)
	return returnDevicesRequestMap
	
def joinDevicesDevices(devices):
	devicedevice = {}
	for key1, value1 in devices.items():
		for key2, value2 in devices.items():
			devicedevice[key1+'-'+key2] = roqatClasses.DeviceDevice(value1, value2)
	return devicedevice
	
def divideIntoGroups(requestPerDevices, devicesFiltered):
	return [devicesFiltered]
	
def filterDevices(requestPerDevices, devices):
#	returnDevices = filterConditions.requestBound(requestPerDevices, devices, 1);
#	print ('Wyfiltrowano devices do ', len(returnDevices))
#	returnDevices = filterConditions.labelBound(requestPerDevices, devices, 1);
	print ('Wyfiltrowano devices do ', len(devices))
	
	return devices
	
def joinDevicesDevicesColumns(devices, devicesGroup, columns):
	devicedevice = {}
	if len(devicesGroup) == 1:
		for key1, value1 in devices.items():
			for key2, value2 in devices.items():
				attributesList={}
				for columnName in columns:
					attributesList[columnName+'1'] = value1[columnName]
					attributesList[columnName+'2'] = value2[columnName]
				devicedevice[key1+'-'+key2] = attributesList
	else:
		for i1, item in enumerate(devicesGroup):
			for i2 in range(i1 + 1, len(devicesGroup)):
				for key1, device1 in item.items():
					for key2, device2 in devicesGroup[i2].items():
						attributesList={}
						for columnName in columns:
							attributesList[columnName+'1'] = device1[columnName]
							attributesList[columnName+'2'] = device2[columnName]
					devicedevice[key1+'-'+key2] = attributesList
		
	return devicedevice
	
