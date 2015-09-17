import collections
import numbers
import csv

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

    def printDMatrixToFile(self, data_path, dest_path):
        with open(data_path, 'rb') as csvfile:
            data = csv.reader(csvfile, quotechar='|')
            with open(dest_path, 'w') as file:
                headers = next(data, None)
                prediction = headers.index('the_same_user_id')
                for attrs in data:
                    file.write(str(0) + ':' + str(self.values_maps[0].index_of(attrs[prediction])) + ',')
                    del attrs[prediction]
                    for i, attr in enumerate(attrs):
                        if self.isFloat(attr):
                            file.write(str(i + 1) + ':' + str(attr) + ',')
                        else:
                            file.write(str(i + 1) + ':' + str(self.values_maps[i+1].index_of(attr)) + ',')
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
   


training_set_creator = TrainingSetToFile()
training_set_creator.printDMatrixToFile('cartesian_product.csv','DMatrixData.txt')