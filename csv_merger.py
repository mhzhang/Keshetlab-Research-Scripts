#!/usr/bin/env python

#Created by MoHan
#Last modification date: Nov 30, 2016
#Contact: mohan_z@hotmail.com
#Sample Usage: python csv_merger.py -p csv_test/ -o sample



import os

import glob
import csv
import codecs
import time
import threading
import subprocess
import numpy as NP
from optparse import OptionParser



csvFolder = './'
outFile = ''



parser = OptionParser()
parser.add_option("-p", "--path", action="store", type="string", dest="csvFolder", help="path to folder with csv files", metavar="CSV")
parser.add_option("-o","--output", action="store", type="string", dest="outFile", help="the file to store output merges", metavar="OUTPUT")


# Options parsing
(options, args) = parser.parse_args()

if options.csvFolder:
	csvFolder = options.csvFolder
if options.outFile:
	outFile = options.outFile



def merge_csv(csvFolder,outFile):
	# Function that executes pif_extract_features.py for all given pif files
	print outFile
	print csvFolder
	with open(outFile+".csv","wb") as csvfile:
		writeEverything = True
		writer = csv.writer(csvfile)
		cell_id = 0
		for p in os.listdir(csvFolder):
			if p.endswith('.csv') and p.startswith('M'):
				print p
				with open(csvFolder+p) as file:
					reader = csv.reader(file)
					h = 0
					i = 0
					if writeEverything:
						for row in reader:
							if (h >= 3) and (h <= 8):
								print row
								writer.writerow(row)
							elif (h >= 11):
								writer.writerow(row)
								cell_id+=1
							h+=1
						writeEverything = False
					else:
						for row in reader:
							if i >= 12: #Should be 13th row but omitting blank row gives 12th
								line = row
								line[0] = cell_id
								writer.writerow(line)
								cell_id+=1
							i+=1




merge_csv(csvFolder,outFile)

