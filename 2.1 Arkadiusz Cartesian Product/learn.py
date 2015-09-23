# pip install xgboost

# git clone https://github.com/dmlc/xgboost.git
# cd xgboost
# ./bulid
# cd python-package
# python setup.py install



import xgboost as xgb

dtrain = xgb.DMatrix('DMatrixData.txt')
dtest = xgb.DMatrix('DMatrixData2.txt')

watchlist  = [(dtest,'eval'), (dtrain,'train')]
param = {'max_depth':2, 'eta':1, 'silent':1, 'objective':'binary:logistic' }

num_round = 2
bst = xgb.train(param, dtrain, num_round, watchlist)

dtest2 = xgb.DMatrix('DMatrixData3.txt')
ypred = bst.predict(dtest2)

print ypred
