import sys, os, re


# Get input and output file names
if len(sys.argv) == 3:
    infile_name = sys.argv[1]
    outfile_name = sys.argv[2]
else:
    infile_name = input("In file: ")
    outfile_name = input("Out file: ")


# Check if input file exists
if not os.path.exists(infile_name):
    sys.exit('ERROR: File %s was not found!' % infile_name)


# Open streams to files
infile = open(infile_name, 'r')
outfile = open(outfile_name, 'w')

# Function to make a tex tabular from a list of lists
def getTexTab(tab):
    colMax = len(max(tab, key=len))
    texOut = "\\vspace{0.4cm}\n\\begin{tabular}{" + ("|l"*colMax) +"|} \\hline\n"

    for row in tab:
        lastSpan = colMax - len(row)
        if lastSpan == 0:
            texOut += ' & '.join(row) + " \\\\ \\hline\n"
        else:
            texOut += ' & '.join(row[:-1])
            if not lastSpan+1 == colMax:
                texOut += ' & '
            texOut += '\multicolumn{%d}{|l|}{%s} \\\\ \\hline\n' % (lastSpan+1, row[-1])

    texOut += "\\end{tabular}\n\\vspace{0.8cm}\n"
    return texOut


# Initialize empty tabular
intab = False
currentTab = []

# Run through lines and make wiki tabulars to tex
for fullLine in infile:
    line = fullLine.strip()

    # Start of new tabular
    if line.startswith('!|') and not intab:
        intab = True
        cols = [x.strip() for x in line[2:-1].split('|')]
        currentTab.append(cols)

    # Continue a tabular
    elif line.startswith('|'):
        intab = True
        cols = [x.strip() for x in line[1:-1].split('|')]
        currentTab.append(cols)
        
    else:
        # Finish and output tabular 
        if intab:
            texOut = getTexTab(currentTab)
            intab = False
            currentTab = []

            # Write tabular
            outfile.write(texOut)

        # Write current line
        if not line.startswith('!'):
            if len(line) > 0:
                outfile.write("\\noindent ")
            outfile.write(fullLine)


# Print final tabular if one was underway when it finished all lines
if intab:
    texOut = getTexTab(currentTab)
    outfile.write(texOut)


# Close files
infile.close()
outfile.close()
