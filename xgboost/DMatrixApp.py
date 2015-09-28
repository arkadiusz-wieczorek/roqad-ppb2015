import collections
import numbers
import csv
import re
import sys

class Mapper:
    def __init__(self):
        self.number_to_value = {}
        self.value_to_number = {}
        self.maxkey = 0
        self.add('T', 1)
        self.add('F', 0)
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

    def printDMatrixTestToFile(self, data_path, dest_path, res_path):
        csvfile =  open(data_path, 'rb')
        data = csv.reader(csvfile, quotechar='|')
        writefile =  open(dest_path, 'w')
        resfile = open(res_path, 'w')
        headers = next(data, None)
        prediction = headers.index('the_same_user_id')
        for attrs in data:
            resfile.write(str(attrs[prediction]) + '\n')
            writefile.write('1' + ' ')
            del attrs[prediction]
            for i, attr in enumerate(attrs):
                if not attr == 'X':
                    if self.isFloat(attr):
                        writefile.write(str(i + 1) + ':' + str(attr).replace(" ", "") + ' ')
                    else:
                        writefile.write(str(i + 1) + ':' + str(self.values_maps[i+1].index_of(attr)) + ' ')
            writefile.write('\n')
        csvfile.close()
        writefile.close()
        resfile.close()

    def printDMatrixToFile(self, data_path, dest_learn_path, dest_test_path):
        csvfile =open(data_path, 'rb')
        data = csv.reader(csvfile, quotechar='|')
        learnfile = open(dest_learn_path, 'w')
        testfile = open(dest_test_path, 'w')
        headers = next(data, None)
        prediction = headers.index('the_same_user_id')
        for line, attrs in enumerate(data):
            if line % 10 == 0 :
                writefile = testfile
            else:
                writefile = learnfile
            writefile.write(str(self.values_maps[0].index_of(attrs[prediction])) + ' ')
            del attrs[prediction]
            for i, attr in enumerate(attrs):
                if not attr == 'X':
                    if self.isFloat(attr):
                        writefile.write(str(i + 1) + ':' + str(attr).replace(" ", "")  + ' ')
                    else:
                        writefile.write(str(i + 1) + ':' + str(self.values_maps[i+1].index_of(attr)) + ' ')
            writefile.write('\n')
        csvfile.close()
        learnfile.close()
        testfile.close()


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
        with open(data_path, 'rb') as csvwritefile:
            data = csv.reader(csvwritefile, quotechar='|')
            with open(dest_path, 'w') as writefile:
                headers = next(data, None)
                prediction = headers.index('the_same_user_id')
                for attrs in data:
                    writefile.write(str(attrs[prediction]) + '\n')

   


training_set_creator = TrainingSetToFile()

print 'Creating DMatrix learning data'
#uczacy
training_set_creator.printDMatrixToFile(sys.argv[1],sys.argv[3] + 'DMatrixDataLearn.txt', sys.argv[3] + 'DMatrixDataTest.txt')

#testowy
# training_set_creator.printDMatrixToFile('../intermediate/result_cartesian_test.csv','../intermediate/DMatrixDataTest.txt')

print 'Creating DMatrix verification data'
#sprawdzajacy
training_set_creator.printDMatrixTestToFile(sys.argv[2],sys.argv[4] + 'DMatrixDataCheck.txt',sys.argv[4] + 'resp.txt')

# training_set_creator.printResponses(sys.argv[2],sys.argv[4] + 'resp.txt')




