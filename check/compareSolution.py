import statistics
import sys
import csv


def checkNormalizedFiles(pred , resp):
    tp,tn,fp,fn = 0,0,0,0
    with open(pred,'r') as predData:
        with open(resp,'r') as realData:
            pred = next(predData, None)
            real = next(realData, None)
            while pred:
                if pred == real:
                    if real == '0\n':
                        tn += 1
                    else:
                        tp += 1
                else:
                    if real == '0\n':
                        fp += 1
                    else:
                        fn += 1
                pred = next(predData, None)
                real = next(realData, None)
    stat = statistics.Statistics(tp=tp, tn=tn, fn=fn, fp=fp)
    return stat.f1()



def normalize(filename):
    fileData = open(filename,'r')
    line = next(fileData, None)
    trueValue = ['T\n', '"T"\n']
    falseValue = ['F\n', '"F"\n']
    if(line == '0\n' or line == '1\n'):
        return filename
    elif(line not in trueValue and line not in falseValue):
        print 'Can\'t compare files'
        fileData.close()
        return filename
    else:
        fileDataN = open(filename + 'Norm','w')
        while(line):
            if line in trueValue :
                fileDataN.write('1\n')
            else:
                fileDataN.write('0\n')
            line = next(fileData, None)
        fileDataN.close()
        fileData.close()
        return filename + 'Norm'

def createResp(data_path, dest_path, column = 'the_same_user_id'):
    with open(data_path, 'rb') as csvfile:
        data = csv.reader(csvfile, quotechar='|')
        with open(dest_path, 'w') as writefile:
            headers = next(data, None)
            prediction = headers.index(column)
            for attrs in data:
                writefile.write(str(attrs[prediction]) + '\n')

def compare(pred, resp, folder, mode):
    if mode == 'csv':
        createResp(resp, folder + 'resp.txt')
    elif mode == 'data':
        createResp(pred, folder + 'pred.txt', column = '"predict"')
        print checkNormalizedFiles(normalize(folder + 'pred.txt') , normalize(resp))
    else:
        print checkNormalizedFiles(normalize(pred) , normalize(resp))

print 'Computing F1'
compare(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
