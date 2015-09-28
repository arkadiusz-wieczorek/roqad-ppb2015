#!/usr/bin/env python

import sys

import add_user_id_to_choosen_dataset as add_id
import cartesian_product as cart_prod
import random_sample_from_dataset as random

multiplier = 1

print "Only ", (multiplier * 100), "%"
random_sample = random.getSample(sys.argv[2] + 'balanced.csv', multiplier, 1) #second parameter % from dataset
dataset_with_id = add_id.addUserID(random_sample, sys.argv[1] + 'labels.csv', 0)
#dataset_with_id = add_id.addUserID(sys.argv[2] + 'balanced.csv', sys.argv[1] + 'labels.csv', 1)
print "computing cartesian product..."
print "!!!", sys.argv[2] + 'result_cartesian.csv'
cart_prod.cartesianProduct(dataset_with_id, sys.argv[2] + 'device_urls.csv', sys.argv[2] + 'result_cartesian.csv')



print "ready!"
