#!/usr/bin/python

from time import gmtime, strftime
import sys
import csv
import copy
import cvsReader
import cvsWriter
import dataHandler
import datetime
import devicesAttributesHandler
import devicesXdevicesAttributesHandler
import roqatClasses

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

#Read files with devices and request

if len(sys.argv) >2:
	devices, request = cvsReader.readFiles(sys.argv[1], sys.argv[2])
else:
	print ('Podaj nazwy plików z devices i request')
	devices = {}
	request = {}


print ('Read devices:', len(devices)) 
print ('Read request:', len(request))

print ('Łącze zapytania z urządzeniami')
requestPerDevices = dataHandler.joinRequestDevices(devices, request)   #Mapa {device-id}, {obiekt DevicesRequest z listą requestów}
print ('Połączono urządzeń z zapytaniami ', len(requestPerDevices))

#Divide devices into groups
devicesFiltered = dataHandler.filterDevices(requestPerDevices, devices)
print ('Po przefiltrowaniu pozostało ', len(devicesFiltered))
devicesGroups = dataHandler.divideIntoGroups(requestPerDevices, devicesFiltered)
print ('Podzielono na ', len(devicesGroups) ,' grup.')

#Manipulate data calculate attributes
devicesExtended = copy.deepcopy(devicesFiltered)   								#Mapa {device-id}, {mapa z kolumna z csv : wartosc}
#devicesXdevicesExtended = dataHandler.joinDevicesDevicesColumns(devicesFiltered, devicesGroups, ['device_id'])    #Mapa {device-id1-device-id2}, {lista atrybutów}

#Add data to devices
devicesExtended = devicesAttributesHandler.addLinksToDevices(requestPerDevices, devices)

#Add data to devices x devices file
#devicesXdevicesExtended = devicesXdevicesAttributesHandler.addAttributeYYY(devicesXdevicesExtended, devicesFiltered)

#Produce new cvs file
#devicesExtended
fileOneName = 'devicesExtended' + strftime('%H%M%m%d%Y', gmtime()) + '.csv'
fileTwoName = 'devicesXdevicesExtended' + strftime('%H%M%m%d%Y', gmtime()) + '.csv'
cvsWriter.writeFile(fileOneName, devicesExtended, ["device_id"])
#cvsWriter.writeFile(fileTwoName, devicesXdevicesExtended, ["device_id1", "device_id2"])
cvsWriter.generateAndWriteToFile(fileTwoName, ["device_id1", "device_id2"])

#Invoke tree algorihtm
#TBA

#Produce files to evaluate f1 f1/2
#TBA