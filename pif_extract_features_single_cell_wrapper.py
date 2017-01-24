#!/usr/bin/env python

#Created by MoHan Zhang
#Last modification date: Nov 30, 2016
#Contact: mohan_z@hotmail.com
#Sample Usage: python pif_extract_features_single_cell.py -p pifFolder/MIAPaCa_3.pif -o output/ -n 6
#


import os
import glob
import time
import threading
import subprocess
import numpy as NP
from optparse import OptionParser


pifFile = ''
startTime, endTime = None, None
numCells = 0


parser = OptionParser()
parser.add_option("-p", "--path", action="store", type="string", dest="pifFile", help="path to PIF file", metavar="PIF")
parser.add_option("-n","--numcells", action="store", type="int", dest="numCells", help="number of cells, check the pif file ", metavar="NUMCELLS")

parser.add_option("-o","--output", action="store", type="string", dest="outputfolder", help="the folder to store output plots", metavar="OUTPUT")
parser.add_option('-r', "--rewrite", action="store_true", dest="rewrite", help="rewrite old files", default=False)

# Options parsing
(options, args) = parser.parse_args()
if options.pifFile:
	pifFile = options.pifFile
if options.numCells is not None:
	numCells = options.numCells

if options.outputfolder:
	outFolder = options.outputfolder
else:
	outFolder = pifFolder
if options.rewrite:
	rewrite = True
else:
	rewrite = False


def run_pif_extract_features_single_cells(pifFile,outFolder, numCells):
	# Function that executes pif_extract_features.py for all given pif files
	print outFolder
	print pifFile

	outParent = outFolder+'/'+pifFile.split('/')[1].split('.')[0]+'/'+'IndividualCells'
	if not os.path.isdir(outParent):
		os.mkdir(outParent)

	for i in range(1,numCells+1):
			outind = outFolder+'/'+pifFile.split('/')[1].split('.')[0]+'/'+'IndividualCells/'+'CellID_'+str(i)+'/'
			os.mkdir(outind)
			print outind
			subprocess.call(['python', 'pif_extract_features.py',
				'-i', pifFile,
							 '-o', outind,
				'-l', '1601',
				'-w', '1201',
				'-S', '5',
				'-T%d' %i])

run_pif_extract_features_single_cells(pifFile,outFolder, numCells)

