import sys, os, re

'''
Author: Kasper 
Inspiration: Martins fit_to_tex.py
This script is made to convert crc .txt files to crc .tex files.
Usages: python crc_to_tex.py <input>.txt <output>.tex
'''

infile_name = ''
#Get input and output file names
if len(sys.argv) == 3:
    infile_name = sys.argv[1]
    outfile_name = sys.argv[2]
else:
    try: 
    	infile_name = input("In file: ")
    	outfile_name = input("Out file: ")
    except:
    	sys.exit('ERROR: please intup name of file. Ex. crc_to_tex.py <input.txt> <output.tex>')


def xstr(list, number):
	try:
		return list[number]
	except:
		return ' '
		
# Check if input file exists
if os.path.exists(infile_name) is False:
	sys.exit('ERROR: File %s was not found!' % infile_name)

#Open streams to files
infile = open(infile_name, 'r')
outfile = open(outfile_name, 'w')

#Initialise empty tabular
Responsibility = []
Collaboration = []

#Run through lines and make wiki tabulars to tex
for fullLine in infile:
    line = fullLine.strip()
	
    #Start of new tabular
    if line.startswith('Class:'):
    	texOut = "\\vspace{0.4cm}\n\\begin{tabular}{|p{7cm}|p{7cm}|} \\hline\n"
        texOut += '\multicolumn{2}{|l|}{Class: %s} \\\\ \\hline\n' % (str(line.split(':')[1]))
    
    elif line.startswith('Responsibility:'):
    	for res in line.split(':')[1].split(';'):
    		Responsibility.append(res)
    
    elif line.startswith('Collaboration:'):
    	for col in line.split(':')[1].split(';'):
    		Collaboration.append(col)

#Make sure we get the right lenght 
runs = len(Responsibility)
if runs < len(Collaboration):
	runs = len(Collaboration)
texOut += '%s & %s \\\\ \\hline\n' %('Responsibility: ','Collaboration: ')

for number in range(runs):
	texOut += '%s & %s \\\\ \n' %(xstr(Responsibility,number),xstr(Collaboration,number))

texOut += "\\hline\n\\end{tabular}\n\\vspace{0.8cm}\n"
	
outfile.write(texOut)

#Close files
infile.close()
outfile.close()
