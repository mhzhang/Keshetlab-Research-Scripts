#!/usr/bin/env python

#Modified by MoHan
#Last modification date: Nov 30, 2016
#Contact: mohan_z@hotmail.com
#Sample Usage: python pif_extract_features_wrapper.py -p pifFolder/ -o output/



import os
import glob
import time
import threading
import subprocess
import numpy as NP
from optparse import OptionParser


pifFolder = ''
startTime, endTime = None, None
threads = 1


parser = OptionParser()
parser.add_option("-p", "--path", action="store", type="string", dest="pifFolder", help="path to folder with PIF files", metavar="PIF")
parser.add_option("--start", action="store", type="int", dest="start", help="first time to process", metavar="START")
parser.add_option("--end", action="store", type="int", dest="end", help="last time to process", metavar="END")
parser.add_option('-t', "--threads", action="store", type="int", dest="threads", help="number of threads to run", metavar="THREAD")
parser.add_option("-o","--output", action="store", type="string", dest="outputfolder", help="the folder to store output plots", metavar="OUTPUT")
parser.add_option('-r', "--rewrite", action="store_true", dest="rewrite", help="rewrite old files", default=False)

# Options parsing
(options, args) = parser.parse_args()
if options.pifFolder:
	pifFolder = options.pifFolder
if options.start is not None:
	startTime = options.start
else:
	startTime = 0
if options.end is not None:
	endTime = options.end
else:
	endTime = 9999999
if options.threads:
	threads = options.threads
if options.outputfolder:
	outFolder = options.outputfolder
else:
	outFolder = pifFolder
if options.rewrite:
	rewrite = True
else:
	rewrite = False


def run_pif_extract_features(pifFolder,outFolder):
	# Function that executes pif_extract_features.py for all given pif files
	print outFolder
	print pifFolder
	for p in os.listdir(pifFolder):
		if p.endswith('.pif'):


		# Check if the file already exists, only run the function if the file doesn't exist yet
			pif = pifFolder+p
			print pif
			outind = outFolder+'/'+p.split('.')[0]+'/'
			os.mkdir(outind)
			print outind

			subprocess.call(['python', 'pif_extract_features.py',
				'-i', pif,
							 '-o', outind,
				'-l', '1200',
				'-w', '1600',
				'-S', '5',
				'-p', '-v', '-m'])

run_pif_extract_features(pifFolder,outFolder)

