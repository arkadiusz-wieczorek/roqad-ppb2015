 #!/usr/bin/env python
import fileinput
import random

def getSample(dataset_file, percent_sample, mode):
	if mode == 1:
		f=open(dataset_file)
		dataset = f.readlines()
	else:
		dataset = dataset_file

	array_length = len(dataset) - 1 #without domain row
	number_of_samples = int(array_length*percent_sample)

	if(percent_sample==1):
		return dataset
	
	samples = []
	samples.append(dataset[0])
	dataset = dataset[1:]
	
	sample = ""
	for x in range(number_of_samples):
		sample = random.choice(dataset)
		samples.append(sample)
	pass
	return samples
