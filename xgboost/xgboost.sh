python DMatrixApp.py ../intermediate/result_cartesian.csv ../intermediate-ver/result_cartesian.csv ./ ./ &&
python learn.py ./ ./ &&

python ../check/compareSolution.py ./prediction.txt ./resp.txt ./ 1