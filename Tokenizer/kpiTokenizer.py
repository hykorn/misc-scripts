#========================================================================
# Description: Uses the Tokenizer to tokenize the formula and attributes
#              Tokenizer based on E. W. Bachtal's algorithm, found here:
#
#                  http://ewbi.blogs.com/develops/2004/12/excel_formula_p.html
#
#              Dependencies:
#              1. KPIINPUTFILE:
#                 - Single column text file of KPI formula (copied from Excel)
#              2. TABDELIMITEDHASHMAP (from Excel saved as tab delimited): 
#                 - Two columns text file consisting of
#                 i. Original KPI name
#                 ii.Post processed KPI name (by Generic Rules Template)
#                 
#              Output:
#              KPIOUTPUTFILE:
#              - Single column text file of the formulas, empty lines
#                removed.
#
#      Author: HY
#   Copyright: Algorithm (c) E. W. Bachtal, (c) R. Macharg
#
#
# Modification History
#
# Date         Author Comment
# =======================================================================
# 22/5/2014    - Initial release
#========================================================================


from termcolor import colored
import re

TMPOUTFILE = "out.txt"
KPIINPUTFILE = "kpi.txt"
TABDELIMITEDHASHMAP = "Book1.txt"
KPIOUTPUTFILE = "kpi_out.txt"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# read KPI formula from KPI file
# File should be in just 1 column of formula
# Parsed and replaced file will be written to out.txt
with open(TMPOUTFILE,"wt") as fout:
    with open(KPIINPUTFILE,"rt") as fin:
        for line in fin:
            p = ExcelParser()
            p.parse(line)
            fout.write(p.extractFunctions())

# read Book1.txt (tab delimited) and store them into a hash map
attrHash = {}
with open(TABDELIMITEDHASHMAP,"rt") as fin:
    for line in fin:
        kpiLabel, kpiName = [a.strip() for a in line.split('\t')]
        attrHash.setdefault('\"'+kpiLabel+'\"','\"'+kpiName+'\"')

#print attrHash


# Replace attributes in formula that is a derived KPI
lineReplaceCount = 0
attrReplaceCount = 0

with open(KPIOUTPUTFILE,"wt") as fout:
    with open(TMPOUTFILE,"rt") as fin:
        lines = filter(None, (line.rstrip() for line in fin))
        for idx, line in enumerate(lines):
            count = 0
            #print "Current line: " + line
            for attributeName, kpiName in attrHash.iteritems():
                #print "Current hashed attr: " + attributeName
                if attributeName in line:
                    line = line.replace(attributeName,kpiName)
                    attrReplaceCount += 1
                    count = 1
                    print colored("Formula:\t",'red')+line
                    print bcolors.OKGREEN+"AttrReplaced:\t"+bcolors.ENDC+attributeName
            lineReplaceCount += count
            fout.write(line+'\n')

print "Lines Replaced: " + str(lineReplaceCount)
print "Total Attributes Replaced: " + str(attrReplaceCount)

