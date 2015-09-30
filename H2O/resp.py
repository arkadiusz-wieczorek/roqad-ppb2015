import sys
import csv

def printResponses(data_path, dest_path):
    with open(data_path, 'rb') as csvwritefile:
        data = csv.reader(csvwritefile, quotechar='|')
        with open(dest_path, 'w') as writefile:
            headers = next(data, None)
            prediction = headers.index('the_same_user_id')
            for attrs in data:
                writefile.write(str(attrs[prediction]) + '\n')

printResponses(sys.argv[1],sys.argv[2])