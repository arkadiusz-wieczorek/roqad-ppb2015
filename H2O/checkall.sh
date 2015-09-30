 touch checkallResult.txt &&

python resp.py ../intermediate-ver/result_cartesian.csv ./resp.txt &&

echo "network : " > checkallResult.txt &&
python ../check/compareSolution.py ./result_network.csv ./resp.txt ./ 1 >> checkallResult.txt &&

echo "predictionGradiendBoostingMachine : " >> checkallResult.txt &&
python ../check/compareSolution.py ./predictionGradiendBoostingMachine.csv ./resp.txt ./ data >> checkallResult.txt

echo "predictionNaiveBayes : " >> checkallResult.txt &&
python ../check/compareSolution.py ./predictionNaiveBayes.csv ./resp.txt ./ data >> checkallResult.txt &&

echo "results : " >> checkallResult.txt &&
python ../check/compareSolution.py ./results.csv ./resp.txt ./ data >> checkallResult.txt &&

echo "resultsDeepLearning : " >> checkallResult.txt &&
python ../check/compareSolution.py ./resultsDeepLearning.csv ./resp.txt ./ data >> checkallResult.txt &&

cat checkallResult.txt &&

rm pred.txt &&
rm pred.txtNorm