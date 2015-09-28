#!/bin/bash

rm ./1.1.Marcin\ Java/result.csv 
rm ./2.1\ Arkadiusz\ Cartesian\ Product/result_cartesian.csv 

cd  ./1.1.Marcin\ Java/src/Data/ &&

javac Main.java && java Main ../../../roq-ad-data-set/learning-set/  ../../../intermediate/ ../../../intermediate/balanced.csv &&

cd ../../../intermediate

#cat balanced.csv | head -n 100 > balanced_trimmed.csv
#mv balanced_trimmed.csv balanced.csv

cd ../1.3\ Lukasz\ python/ && 

python3 roqat.py ../roq-ad-data-set/learning-set/devices.csv ../roq-ad-data-set/learning-set/requests.csv ../intermediate/device_urls.csv &&


cd ../1.2\ Matematycy\ R/

echo "generating clusters..."
Rscript clustering.R ../intermediate/balanced.csv ../intermediate/device_urls.csv ../intermediate/balanced_with_cluster.csv &&

cd ../intermediate

sed -i 's/NA//g' balanced_with_cluster.csv
sed -i 's/\"//g' balanced_with_cluster.csv
sed -i 's/ //g' balanced_with_cluster.csv

mv -f balanced_with_cluster.csv balanced.csv

cd ../2.1\ Arkadiusz\ Cartesian\ Product &&
python app.py ../roq-ad-data-set/learning-set/ ../intermediate/
