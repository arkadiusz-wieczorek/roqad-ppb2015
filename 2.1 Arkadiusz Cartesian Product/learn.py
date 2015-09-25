# pip install xgboost

# git clone https://github.com/dmlc/xgboost.git
# cd xgboost
# ./bulid
# cd python-package
# python setup.py install



import xgboost as xgb
import numpy as numpy

threshold = 0.5


dtrain = xgb.DMatrix('../intermediate/DMatrixDataLearn.txt')
dtest = xgb.DMatrix('../intermediate/DMatrixDataTest.txt')

watchlist  = [(dtest,'eval'), (dtrain,'train')]
# param = {'max_depth':30, 'eta':1, 'objective':'binary:logistic', 'num_class': 2 }
param = {'max_depth':8, 'eta':1, 'objective':'binary:logistic'}   
num_round = 2
bst = xgb.train(param, dtrain, num_round, watchlist)

dtest2 = xgb.DMatrix('../intermediate/DMatrixDataCheck.txt')
ypred = bst.predict(dtest2)

with open('../intermediate/prediction.txt', 'w') as predfile:   
    for value in ypred:
        predfile.write(str(int(round(value))) + '\n')

# numpy.savetxt('../intermediate/prediction.txt', ypred, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ')
