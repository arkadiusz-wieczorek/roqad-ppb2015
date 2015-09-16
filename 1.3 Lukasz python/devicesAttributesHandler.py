def addLinksToDevices(requestPerDevices, devices):				
	returnDevices={}
	for key, device in devices.items():
#		print (key , ' ', devicesUser[key], ' ',len(userDevices[devicesUser[key]].devices))
				urlList = []
				for requestSingle in requestPerDevices[key].request:
					urlList.append(requestSingle['url'])
				devices[key].update({'urlList' : urlList})
#				devices[key].update({'request' : requestPerDevices[key].request})
				returnDevices[ key ] = {'device_id': devices[key]['device_id'], 'urlList': devices[key]['urlList']}
#				returnDevices[ key ] = devices[key]
			
	return returnDevices