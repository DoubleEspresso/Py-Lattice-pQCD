#!/usr/bin/python
# -*- python -*-   
# $RCSfile: main.py,v $
"""
Usage: python main.py [Options]

Routine to compute 1-loop lattice integrals in perturbation theory.
This file reads diagram.in, calls mathematica to taylor expand the integrand
according to pre-computed feynman rules, and writes results to disk.  

Options:
  --f,file  : writes the result to user defined file.

  --t,trace : traces over all Dirac matrices in the integrand.
"""

_author__ = "M. Glatzmaier"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 1/1/2012 16:00:22 $"
__copyright__ = "Copyright (C) 2012 M. Glatzmaier"
__licence__ = """This file is covered by the GPL v2 (see LICENSE file)."""

import sys
import os
import re
import math
import subprocess
from subprocess import Popen
from optparse import OptionParser

#-----------------------------------
import reader
import io
import tensors

#-----------------------------------

#------------------------------------------
#- Main -
#------------------------------------------
    
if __name__ == "__main__":
 from sys import argv,exit

#-----pass options-------
 parser = OptionParser()
 
 parser.add_option("-f", "--file", action="store", dest="filename",default="Formatted_Data.txt",
                   help="stores resulting formatted data in given file.")
                    
 parser.add_option("-t", "--trace", action="store_true", dest="trace", default = False,
                   help="trace over lorentz indices in numerator.")


 (options, args) = parser.parse_args()

 

#----------------------------------
# initialize various classes
IO = io.IO()
Tensor = tensors.Tensor()
Reader = reader.Reader()

# collect the options from diagram.in
# may not always want to read from diagram.in
# in this case, we should add a parser option
read_options = Reader.read_diagram()

# format the initial expression for FORM
expr = IO.parse()

#-----------------------------------------------------------
# read the input file diagram.in and call mathematica
# to create the math.in file (taylor expanded feynman rules)
# for the diagram of interest


#-------------------------------------------------
# now we export to FORM to have the following simplifications made
# 1. expand and collect desired power in 'a'
# 2. simplify the products of dirac matrices
expr = IO.write_form_file(expr, "EXPAND")

#---------------------------------------------------
# if trace flag set, we trace over dirac matrices,
# otherwise we expand and simplify
#if (options.trace == False):
if (read_options["Trace"] == "false"):
    expr = IO.write_form_file(expr, "DIRAC_SIMPLIFY")
else:
    expr = IO.write_form_file(expr, "DIRAC_TRACE")


#------------------------------------------------
# now we contract all indices in the expression
# using python scripts instead of FORM
expr = Tensor.contract(expr)


#------------------------------------------------
# now we again move the expression to FORM to 
# organize the kh-powers using 
# 1. symmetry tables/expansion -- FORM
# 2. index contract in python 
# 3. append sums in python
expr = IO.write_form_file(expr,"APPLY_SYMMETRY_TABLES")

expr = Tensor.contract(expr)

expr = IO.write_form_file(expr, "EXPAND")

expr = IO.write_form_file(expr,"REPLACE_B_TERMS")


# main routine to prep the expression for integration
expr = Tensor.append_sums(expr,read_options)



# one final expansion to simplify the expression after 
# all manipulations have been completed (often very helpful)
expr = IO.write_form_file(expr, "EXPAND")



#--------------------------------------------------
# write the expression to the integration directory
# to be integrated
if (read_options["Integrate"]=="true"):
    ans = IO.integrate_expression(expr,read_options)


    # print the final answer
    print ""
    print "=========================="
    print "Done!"
    print "=========================="
    print ""
    print "J = " + ans
    print ""

    # write results to a log file in case of auto-run script enabled
    with open("auto_run.log","w") as out:
        out.write("J = " + ans)
    out.close()

else:
    print ""
    print "=========================="
    print "Done! Unintegrated Result:"
    print "=========================="
    print expr
    print ""


# // end _main_  //
