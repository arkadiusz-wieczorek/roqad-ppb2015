#!/usr/bin/env python

import shutil
import fileinput
shutil.copyfile("sample_data.tab", "__sample_data.tab")

lines = open("sample_data.tab").readline()
old_line = lines[0:]

first_line = "	__".join([x[0:] for x in lines.split("	")]);
new_first_line =  "__" + first_line

for line in fileinput.input("__sample_data.tab", inplace=True): 
      print line.replace(old_line, new_first_line)