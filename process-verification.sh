#!/bin/bash

rm ./1.1.Marcin\ Java/result.csv 
rm ./2.1\ Arkadiusz\ Cartesian\ Product/result_cartesian.csv 

cd  ./1.1.Marcin\ Java/src/Data/ &&

javac Main.java && java Main ../../../roq-ad-data-set/verification-set/  ../../../intermediate-ver/ ../../../intermediate-ver/balanced.csv &&

cd ../../../intermediate-ver

#cat balanced.csv | head -n 100 > balanced_trimmed.csv
#mv -f balanced_trimmed.csv balanced.csv
#head -n 1 balanced.csv > temp.txt
#head -n -1 balanced.csv > balanced_headless.csv
#perl -ne 'print if(rand() < .1)' balanced_headless.csv >> temp.txt
#mv temp.txt balanced.csv

#trim last, useless line
head -n -1 balanced.csv > balanced.temp.csv &&
mv balanced.temp.csv balanced.csv

#remove \" chars
sed -i 's/\"//g' balanced.csv

cd ../1.3\ Lukasz\ python/ && 

python3 roqat.py ../roq-ad-data-set/verification-set/devices.csv ../roq-ad-data-set/verification-set/requests.csv ../intermediate-ver/device_urls.csv &&

cd ../1.2\ Matematycy\ R/

echo "generating clusters..."
Rscript clustering.R ../intermediate-ver/balanced.csv ../intermediate-ver/device_urls.csv ../intermediate-ver/balanced_with_cluster.csv &&

cd ../intermediate-ver

sed -i 's/NA//g' balanced_with_cluster.csv
sed -i 's/\"//g' balanced_with_cluster.csv
sed -i 's/ //g' balanced_with_cluster.csv

mv -f balanced_with_cluster.csv balanced.csv

cd ../2.1\ Arkadiusz\ Cartesian\ Product &&
python app.py ../roq-ad-data-set/verification-set/ ../intermediate-ver/

cd ../intermediate
echo "DONE!" > done.txt
