#!/usr/bin/python

import sys
import csv
import cvsReader
import cvsWriter
import dataHandler
import devicesAttributesHandler

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

#Read files with devices and request

devices, request = cvsReader.readFiles(sys.argv[0], sys.argv[1])

print 'Read devices:', len(devices) 
print 'Read request:', len(request)

requestPerDevices = dataHandler.joinRequestDevices(devices, request)
devicesXdevices = dataHandler.joinDevicesDevices(devices, devices)

#Manipulate data calculate attributes
devicesExtended = copy.deepcopy(devices)
devicesXdevicesExtended = dataHandler.joinDevicesDevicesIds(devices, devices)

#Add data to devices
devicesExtended = devicesAttributesHandler.addAttributeXXX(devicesExtended)

#Add data to devices x devices file
devicesXdevicesExtended = devicesXdevicesAttributesHandler.addAttributeYYY(devicesXdevicesExtended, devicesXdevices)

#Produce new cvs file
#devicesExtended
cvsWriter.writeFile('devicesExtended.csv', devicesExtended)
cvsWriter.writeFile('devicesXdevicesExtended.csv', devicesXdevicesExtended)

#Invoke tree algorihtm
#TBA

#Produce files to evaluate f1 f1/2
#TBA