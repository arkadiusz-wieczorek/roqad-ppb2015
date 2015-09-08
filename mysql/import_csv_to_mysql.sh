#!/bin/bash
sudo mysqlimport -p roqad ./devices.csv ./labels.csv ./requests.csv --fields-terminated-by=,