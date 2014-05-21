#!/bin/python

import filecmp,sys

filecmp.dircmp(sys.argv[1],sys.argv[2]).report()
