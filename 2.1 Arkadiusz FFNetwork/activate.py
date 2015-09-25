from pybrain.datasets import ClassificationDataSet
from pybrain.datasets import SupervisedDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer
from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal
import pickle


import fileinput


fileObject = open('./network.xml','r')
net = pickle.load(fileObject)


ds = SupervisedDataSet(16,1)

tf = open('./result_cartesian-very-balanced.csv','r');
	

for line in tf.readlines()[1:]:
	data = [float(x) for x in line.split(',') if x != '']
	indata =  data[1:17]
	outdata = data[0:1]
	ds.addSample(indata,outdata)

print map(int, map(abs, map(round, net.activateOnDataset(ds))))

print "ready"
