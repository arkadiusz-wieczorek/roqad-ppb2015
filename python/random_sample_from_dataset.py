 #!/usr/bin/env python
import fileinput
import random

def getSample(dataset_file, percent_sample):
	f=open(dataset_file)
	dataset=f.readlines()

	array_length = len(dataset) - 1 #without domain row
	number_of_samples = int(array_length*percent_sample)
	sample = ""
	samples = dataset[0]
	
	for x in range(number_of_samples):
		sample = random.choice(dataset)
		samples += sample
	pass
	return samples