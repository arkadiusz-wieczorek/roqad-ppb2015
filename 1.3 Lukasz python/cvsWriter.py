import csv
import os

def writeFile(fileName, data, columnSort):
	if not os.path.exists(os.path.dirname(fileName)):
		os.makedirs(os.path.dirname(fileName))
	with open(fileName, 'w', newline="\n", encoding="utf-8") as csvfile:
		print ('Zapisuje ', len(data))
		if len(data) > 0:
			fieldnames = list(list(data.values())[0].keys())
			for columnName in reversed(columnSort):
				fieldnames.remove(columnName)
				fieldnames.insert(0, columnName)
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for key, value in sorted(data.items()):
				writer.writerow(value)
