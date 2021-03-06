#!/usr/bin/python
# -*- python -*-   
# $RCSfile: auto_integrate.py,v $

#---------------------------
# auto integration script
# used mainly for large expressions
#---------------------------

import os
import sys
import re
import math
import subprocess
from subprocess import Popen
from optparse import OptionParser

import reader
import io
import tensors

# integration modules
sys.path.insert(0,'integrate')
import formatting
import integrate
#--------------- MAIN --------------------------

# read in the options for this diagram
Reader      = reader.Reader()
read_options= Reader.read_diagram()


# change directory
os.chdir("integration")
Integrator  = integrate.Integrator()

# integrate the j-integrals
print "...Integrating"
j_integrals = Integrator.mathematica_integrate(read_options)

# integrate the b-integrals analytically
b_integrals = Integrator.form_integrate(read_options)
Integrator.export(j_integrals+b_integrals)

# prep the integrals.results file for mathematica reps
Integrator.format_results()
ans = Integrator.mathematica_expand(read_options)

os.chdir("../")


print ""
print "==============================="
print "Done!"
print "==============================="
print ""
print "J = " + ans
print ""


# write results to a log file in case of auto-run script enabled
with open("auto_run.log","w") as out:
    out.write("J = " + ans)
    out.close()


# END MAIN

