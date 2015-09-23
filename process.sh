#!/bin/bash

rm ./1.1.Marcin\ Java/result.csv 
rm ./2.1\ Arkadiusz\ Cartesian\ Product/result_cartesian.csv 

cd  ./1.1.Marcin\ Java/src/Data/ &&

javac Main.java && java Main ../../../roq-ad-data-set/learning-set/  ../../../intermediate/ ../../../intermediate/balanced.csv &&

cd ../../../1.3\ Lukasz\ python/ && 

python3 roqat.py ../roq-ad-data-set/learning-set/devices.csv ../roq-ad-data-set/learning-set/requests.csv ../intermediate/device_urls.csv &&

cd ../2.1\ Arkadiusz\ Cartesian\ Product &&
python app.py ../roq-ad-data-set/learning-set/ ../intermediate/
