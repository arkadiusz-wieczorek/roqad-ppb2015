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

    def __init__(self,data):
        self.keys_map = Mapper()
        self.values_maps = collections.defaultdict(Mapper)
        self.data = data
        self.training_data = self.create_training_set(data)
