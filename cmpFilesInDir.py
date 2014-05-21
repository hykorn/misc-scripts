#!/bin/python

import filecmp,os,sys

# Determine the items that exist in both directories
d1_contents = set(os.listdir(sys.argv[1]))
d2_contents = set(os.listdir(sys.argv[2]))
common = list(d1_contents & d2_contents)
uncommon = list(d1_contents ^ d2_contents)
common_files = [ f 
                for f in common 
                if os.path.isfile(os.path.join(sys.argv[1], f))
                ]
print 'Common files:', common_files

# Compare the directories
match, mismatch, errors = filecmp.cmpfiles(sys.argv[1], 
                                           sys.argv[2], 
                                           common_files)
print 'Match:', match
print 'Mismatch:', mismatch
print 'Errors:', errors
