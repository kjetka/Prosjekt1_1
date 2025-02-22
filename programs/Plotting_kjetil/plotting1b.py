from __future__ import division
from numpy import * 
from numpy.linalg import *
from matplotlib.pyplot import*
import glob, os


def filer_funk(): #Stikkord = hvilke filer, Skanntype = n
	skanntype = "n"
	filer = []
	filnavn = []
	for file in glob.glob("*.txt"):
		filer.append(file)
	antall_filer = len(filer)

	
	# filer_med_stikkord =[]
	# legendnavn_med_stikkord = []
	# for fil in filer:
	# 	if stikkord in fil:
	# 		filer_med_stikkord.append(fil)
	# 		legendnavn = fil[fil.find(skanntype):fil.find(skanntype)+4]
	# 		bytte = legendnavn.find('_')
	# 		legendnavn =  legendnavn[0:bytte]+ '='+ legendnavn[bytte+1:]
	# 		legendnavn_med_stikkord.append(legendnavn)
	# return filer_med_stikkord, legendnavn_med_stikkord	#, plotnavn, antall_filer 		#filnavn = filer - .txt

	return filer

print filer_funk()
filer = filer_funk()

for k in range(len(filer)):

	nummerisk = []
	analytisk = []
	feil =[]
	nummerisk.append(0)
	analytisk.append(0)

	with open(filer[k]) as infile:
		for i in range(3):
			firstline = infile.readline()
		
		for line in infile:
			thisline = line.split()
			nummerisk.append(thisline[0])
			analytisk.append(thisline[1])
			feil.append(thisline[2])
	nummerisk.append(0)
	analytisk.append(0)
	n = len(nummerisk)-2
	print n

	x = linspace(0,1,n+2)
	figure(k)
	plot(x,nummerisk, label = "Numerical")
	plot(x, analytisk, label = "Analytical")
	legend()
	title("Plot with the special algorithm, h = %.0e" %(1/float(n)))
	xlabel("x"); ylabel("y")
	savefig("n_%.0f.pdf" %n)
	"""
	figure(5)
	title("Rel.error")
	plot(x,feil, label = n)
	legend()
	savefig("1b_error.pdf")
	"""