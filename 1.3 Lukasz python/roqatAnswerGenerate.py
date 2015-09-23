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
	devices, labels = cvsReader.readFiles(sys.argv[1], sys.argv[2])
else:
	print ('Podaj nazwy plików z devices i request')
	devices = {}
	labels = {}

print ('Read devices:', len(devices)) 
print ('Read request:', len(labels))

print ('£¹cze zapytania z odpowiedziami')
deviceUsers, userDevices = dataHandler.joinLablesDevices(devices, lables)   #Mapa {device-id}, {obiekt DevicesRequest z list¹ requestów}
print ('Po³¹czono urz¹dzeñ z odpowiedziami ', len(deviceUsers))

#Produce new cvs file
#devicesExtended
fileTwoName = 'devicesXdevicesAnswer' + strftime('%H%M%m%d%Y', gmtime()) + '.csv'
cvsWriter.generateAndWriteToFile(fileTwoName, devices, deviceUsers, ["device_id1", "device_id2"])

#Invoke tree algorihtm
#TBA

#Produce files to evaluate f1 f1/2
#TBA