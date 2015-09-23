import collections
import numbers

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

    def printDMatrixToFile(self, data, path):
        with open(path, 'w') as file:
            names = data[0]
            del data[0]
            prediction = names.index('prediction')
            for record in data:
                attrs = record.split(',')
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
   

class Training_set_creator:

    def maptovalue(self,collection):
        for key in collection[1]:
            self.values_maps[key].add('',0)
        for record in collection:
            for key in record:
                if not self.isFloat(record[key]):
                    record[key] = self.values_maps[key].index_of(record[key])
        return collection

    def mapkeys(self,collection):
        returnlist = []
        for record in collection: 
            returnrecord = {}  
            for key in record:
                returnrecord[self.keys_map.index_of(key)] = record[key]
            returnlist.append(returnrecord)
        return returnlist

    def create_training_set(self, data):
        data = self.maptovalue(data)
        return self.mapkeys(data)

    def isFloat(self,string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    def printDMatrixToFile(self, data, path):
        with open(path, 'w') as file:
            for record in data:
                for attr in record:
                    file.write(str(attr) + ':' + str(record[attr]) + ',')
                file.write('\n')
            file.flush()

    def __init__(self,data):
        self.keys_map = Mapper()
        self.values_maps = collections.defaultdict(Mapper)
        self.data = data
        self.training_data = self.create_training_set(data)
