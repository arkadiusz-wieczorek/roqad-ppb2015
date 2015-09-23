class DevicesRequest:
	request = []
	device = {}

	def __init__(self, device, request):
		self.device = device
		self.request = request
	
	def addRequest(self, newRequest):
		self.request.append( newRequest )

class UserDevice:
	devices = []
	user = {}

	def __init__(self, user, devices):
		self.user = user
		self.devices = devices
	
	def addDevice(self, newDevice):
		self.devices.append( newDevice )

class DeviceUser:
	device = []
	users = {}

	def __init__(self, device, users):
		self.users = users
		self.device = device
	
	def addUser(self, newUser):
		self.users.append( newUser )
		
		
class DeviceDevice:
    def __init__(self, deviceOne, deviceTwo):
        self.deviceOne = deviceOne
        self.deviceTwo = deviceTwo
