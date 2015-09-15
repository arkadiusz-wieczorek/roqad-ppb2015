import checksolution
import collections
import csv

def readfile(url):
    data = collections.defaultdict(list)
    with open(url, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            user, device = row[0].split(',')
            data[user].append(device)
    data = list(data.values())
    return data

def readfile2(url):
    data = []
    with open(url, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            data.append(filter(lambda a: a != '', row[0].split(',')))
    return data

def readfile3(url):
    data = []
    with open(url, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            if len(filter(lambda a: a != '', row[0].split(','))) == 1:
                data.append(filter(lambda a: a != '', row[0].split(',')))
    return data


#testdata = readfile2('devices_by_ip.csv')


testdata = readfile('ip_to_device.csv')
realdata = readfile('labels.csv')
checksolution = checksolution.PrepareDataToF1(testdata, realdata)
print checksolution.prepare_to_f1()
# print(checksolution.prepere_to_closest_cluster_f1())