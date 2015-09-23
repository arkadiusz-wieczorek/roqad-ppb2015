import statistics

class PrepareDataToF1:
    def __init__(self, testdata, realdata):
        self.realdata = realdata
        self.testdata = testdata

    def countcommon(self, testdata, realdata):
        matrix = []
        for i, testuser in enumerate(testdata):
            matrix.append([])
            for j, realuser in enumerate(realdata):
               matrix[i].append(len(set(realuser).intersection(set(testuser))))
        return matrix
    
    def countdevices(self,data):
        counted = []
        for user in data:
            counted.append(len(user))
        return counted
    
    def prepare_to_closest_cluster_f1(self):
        common = self.countcommon(self.testdata, self.realdata)
        predicted = self.countdevices(self.testdata)
        real = self.countdevices(self.realdata)
        stat = statistics.Statistics(common_cluster_devices_nos=common, pred_cluster_devices_nos= predicted, true_cluster_devices_nos=real)
        return stat.closest_cluster_f1()


    def prepare_to_f1(self):
        tp,tn,fp,fn = 0,0,0,0
        number_of_devices = 0
        for user in self.realdata:
            number_of_devices += len(user) 
        for realuser in self.realdata:
            for testuser in self.testdata:
                common = len([x for x in testuser if x in realuser])
                if not common == 0:
                    onlyreal = len([x for x in realuser if x not in testuser])
                    onlytest = len([x for x in testuser if x not in realuser])
                    tp += (common * (common - 1))/2
                    tn += number_of_devices - (onlytest + onlyreal + common)
                    fp += common*onlytest
                    fn += common*onlyreal
        stat = statistics.Statistics(tp=tp, tn=tn/2, fn=fn/2, fp=fp/2)
        return stat.f1()