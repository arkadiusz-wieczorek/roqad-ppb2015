import collections
import numbers
import csv
import re

class Mapper:
    def __init__(self):
        self.number_to_value = {}
        self.value_to_number = {}
        self.maxkey = 0
    def index_of(self, x):
        if x not in self.value_to_number:
            self.maxkey += 1
            self.value_to_number[x] = self.maxkey
            self.number_to_value[self.maxkey] = x
        return self.value_to_number[x]
    def value_of(self,x):
        return self.number_to_value[x]
    def add(self, key, index):
        self.value_to_number[key] = index
        self.number_to_value[index] = key


class TrainingSetToFile:

    def printDMatrixTestToFile(self, data_path, dest_path):
        with open(data_path, 'rb') as csvfile:
            data = csv.reader(csvfile, quotechar='|')
            with open(dest_path, 'w') as file:
                headers = next(data, None)
                prediction = headers.index('the_same_user_id')
                for attrs in data:
                    file.write('1' + ' ')
                    del attrs[prediction]
                    for i, attr in enumerate(attrs):
                        if not attr == 'X':
                            if self.isFloat(attr):
                                file.write(str(i + 1) + ':' + str(attr).replace(" ", "") + ' ')
                            else:
                                file.write(str(i + 1) + ':' + str(self.values_maps[i+1].index_of(attr)) + ' ')
                    file.write('\n')

    def printDMatrixToFile(self, data_path, dest_path):
        with open(data_path, 'rb') as csvfile:
            data = csv.reader(csvfile, quotechar='|')
            with open(dest_path, 'w') as file:
                headers = next(data, None)
                prediction = headers.index('the_same_user_id')
                for attrs in data:
                    file.write(str(attrs[prediction]) + ' ')
                    del attrs[prediction]
                    for i, attr in enumerate(attrs):
                        if not attr == 'X':
                            if self.isFloat(attr):
                                file.write(str(i + 1) + ':' + str(attr).replace(" ", "")  + ' ')
                            else:
                                file.write(str(i + 1) + ':' + str(self.values_maps[i+1].index_of(attr)) + ' ')
                    file.write('\n')


    def isFloat(self,string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    def __init__(self):
        self.keys_map = Mapper()
        self.values_maps = collections.defaultdict(Mapper)

    def printResponses(self, data_path, dest_path):
        with open(data_path, 'rb') as csvfile:
            data = csv.reader(csvfile, quotechar='|')
            with open(dest_path, 'w') as file:
                headers = next(data, None)
                prediction = headers.index('the_same_user_id')
                for attrs in data:
                    file.write(str(attrs[prediction]) + '\n')

   


training_set_creator = TrainingSetToFile()


#uczacy
training_set_creator.printDMatrixToFile('../intermediate/result_cartesian_learn.csv','../intermediate/DMatrixDataLearn.txt')

#testowy
training_set_creator.printDMatrixToFile('../intermediate/result_cartesian_test.csv','../intermediate/DMatrixDataTest.txt')

#sprawdzajacy
training_set_creator.printDMatrixTestToFile('../intermediate/result_cartesian_check.csv','../intermediate/DMatrixDataCheck.txt')
training_set_creator.printResponses('../intermediate/result_cartesian_check.csv','../intermediate/resp.txt')




