class Reader:
    def readFromTable(self,sample):
        data = []
        names = []
        for i, attrs in enumerate(sample):
            if i == 0:
                names = attrs.split(',')
            else:
                collection = {}
                attributes = attrs.split(',')
                for j, attr in enumerate(attributes):
                    collection[names[j]] = attr
                data.append(collection)
        return data
