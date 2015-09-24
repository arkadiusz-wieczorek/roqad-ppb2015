import statistics

tp,tn,fp,fn = 0,0,0,0
with open('../intermediate/prediction.txt','r') as predData:
    with open('../intermediate/resp.txt','r') as realData:
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
print stat.f1()
