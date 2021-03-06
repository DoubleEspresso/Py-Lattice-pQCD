#!/usr/bin/python
# -*- python -*-   
# $RCSfile: io.py,v $

#---------------------------
# this is a library for 
# io/formatting from python/
# mathematica/ form
#---------------------------
import os
import tensors
import sys

# integration modules
sys.path.insert(0, 'integration')
import formatting
import integrate

#-------------------------------------------
Tensor = tensors.Tensor()


class IO:
    
    def __init__(self):
        self.file = "tmp.out"

#-------------------------------------------
    def parse(self):

        indata=[]
        expr = ""
        for line in open("math.in",'rb'):
            indata.append(line.strip().replace("\n",""))

        for line in indata:
            expr += line.replace(" ","")

        expr = self.math_to_form(expr)

        return expr

#-------------------------------------------
    def math_to_form(self,expr):
        # assumes the input is one string
        expr = expr.replace("I","i_")
        expr = expr.replace("[","(")
        expr = expr.replace("]",")")
        expr = expr.replace(".","*")
        expr = expr.replace("SUM","sum")
        expr = expr.replace("DB","db")
        expr = expr.replace("DQ","dq")
        expr = expr.replace("AA","aa")
        expr = expr.replace("BB","bb")
        expr = expr.replace("M","m")
        expr = expr.replace("S","s")
        expr = expr.replace("B","b")
        return expr

#-------------------------------------------
    def form_to_math(self,expr):
        expr = expr.replace("i_","I")
        expr = expr.replace("(","[")
        expr = expr.replace(")","]")
        return expr

#-------------------------------------------
    def run_form(self,exe):
        return exe

#-------------------------------------------
    def write_form_file(self,expr,type):
        
        # for each FORM file, we define a header
        # which has all the relevant data defined
        FORM_HEADER ="""*===This file was automatically generated in Python==*\n
off statistics;

*====includes===
#include ../../inc/diracSimplify.h
#include ../../inc/symmetryTables.h
#include ../../inc/replaceBterms.h
#include ../../inc/projectOps.h
#include ../../inc/irIsolate.h
#include ../../inc/expandSums.h
#include ../../inc/expandSumsOverlap.h
#include ../../inc/formIntegrate.h
#include ../../inc/diracTrace.h

*==lorentz indices===
autodeclare index ix =0;
autodeclare index ex =0;

*==polarization indices===
autodeclare index sx = 0;

*==vectors==
CF p,p1,p2,p3,p4;  * // Fermion momenta
CF k;              * // Loop momenta 
CF q,q1,q2,q3,q4;  * // gauge field momenta 
CF d;              * // light-like vector 

* == Special functions == 
CF sum,SUM;         * // index summation helpers 
CF s,S,m,M,b,B,c,C; * // trig functions of loop-momenta


* == Gamma matrices == 
F G;
CF g;
CF c;

* == Symbols ==
S g0, rh, rw, m0, a;  * // physical constants
S pow, pow2, sf, DIM; * // powers/scale factors
S db, dq, aa, bb;     * // bosonic/fermionic denominators
S n,nx,ny,nz,nt;      * // powers of k - used for integrating
S OP;                 * // momentum space operator

* == The expression==
L expr = """ + expr + ";\n"
            

        FORM_FOOTER = """\n
contract;
print expr;
***********
*ANSWER
.end"""
        #---------------------------------------------------------
        # the commands to add based on type            
        # normal form-expand collect those terms a^0
        if (type == "EXPAND"):
            FORM_COMMANDS = """id a^pow?!{-20,0}=0;"""

            FORM_FILE = "form.expand.frm"


        #---------------------------------------------------------
        # simplify products of dirac matrices
        if (type == "DIRAC_SIMPLIFY"):
            FORM_COMMANDS = """\n
#call diracSimplify()
.sort"""


            FORM_FILE = "form.dirac.simplify.frm"
        #-------------------------------------------------------

        if (type == "APPLY_SYMMETRY_TABLES"):
            FORM_COMMANDS = """\n
#call symmetryTables()
.sort
"""
            FORM_FILE = "form.symmetry.frm"
        #-------------------------------------------------------

        if (type == "REPLACE_B_TERMS"):
            FORM_COMMANDS = """\n
#call replaceBterms()
.sort
"""

            FORM_FILE = "form.replaceBterms.frm"
        #-------------------------------------------------------
        # we need to project momentum operators, which means
        # in projectOps() we have to write which kind of momentum
        # structure we want to find...additional code is necessary for that.
        if (type == "IR_ISOLATE"):
            FORM_COMMANDS = """\n
#call expandSums()
.sort

#call irIsolate()
.sort 

#call projectOps()
"""
            FORM_FILE = "form.IRisolate.frm"

        #-------------------------------------------------------
        # we need to project momentum operators, which means
        # in projectOps() we have to write which kind of momentum
        # structure we want to find...additional code is necessary for that.
        if (type == "IR_ISOLATE_OVERLAP"):
            FORM_COMMANDS = """\n
#call expandSumsOverlap()
.sort

#call irIsolateOverlap()
.sort 

#call projectOps()
"""
            FORM_FILE = "form.IRisolateOverlap.frm"



        #-------------------------------------------------------
        # send the output to python/form to be integrated 
        # usually this means integrating using mathematica.
        if (type == "INTEGRATE"):
            FORM_COMMANDS = """\n 

#call formIntegrate(expr)
.sort
"""
            FORM_FILE = "form.integrate.frm"

        #--------------------------------------------------------
        # trace code for fermion loop diagrams
        if (type == "DIRAC_TRACE"):
            FORM_COMMANDS = """\n
#call diracTrace()
.sort
 """
            FORM_FILE = "form.trace.frm"
        #--------------------------------------------------------
        # execute and collect the result from the FORM codes.
        OUT_FILE = open("form.tmp/"+FORM_FILE,"w")
        OUT_FILE.write(FORM_HEADER + FORM_COMMANDS + FORM_FOOTER)
        OUT_FILE.close()

        os.chdir("form.tmp")
        new_expr = os.popen("./form.execute.sh "+FORM_FILE,"r").read().replace(" ","").replace("\n","").replace(";","")
        os.chdir("../")

        return new_expr
        
#-------------------------------------------
    def export_to_mathematica(self,expr):
        return expr

#-------------------------------------------
    def integrate_expression(self,expr,options):

        # we write the expression to integration/tmp.out
        # then cd to the integration directory and call
        # the python routines to collect the integrals
        # and integrate everythin in mathematica.
        os.chdir("integration")
        f = open('tmp.out','w')
        f.write(expr)
        f.close()

        # the integration modules
        Formatter  = formatting.Parser()
        formData   = Formatter.read("FORM")
        vectorData = Formatter.vectorize(formData)

        # get the integrals
        integralVector = Formatter.fetch_integrals(vectorData,options)
        
        # print them to files b_integrals.out, j_integrals.out
        Formatter.export(integralVector)

        # integrate
        #print ""
        #print "...Integrating"
        #print ""
        Integrator  = integrate.Integrator()
        j_integrals = Integrator.mathematica_integrate(options)


        # integrate b-integrals analytically
        b_integrals = Integrator.form_integrate(options)
        Integrator.export(j_integrals+b_integrals)

        # prep the integrals.results file for mathematica reps
        Integrator.format_results()
        ans = Integrator.mathematica_expand(options)

        os.chdir("../")

        return ans 
#-------------------------------------------
    def vectorize(self,expr):
        # script to split the expression into 
        # signed monomial terms, both plus signed and 
        # minus signed data are saved in a vector and returned
        vector_data = []
        expr = expr.replace(' ','')
        expr = expr.replace('^-','{POW}')

        tmp = expr.split('+')

        tmp_minus = []
        tmp_plus  = []

        # negative terms
        for index in range(len(tmp)):
            if tmp[index].find('-') != -1:
                tmp_negative = tmp[index].split('-')
                for j in range(1,len(tmp_negative)):
                    tmp_negative[j] = tmp_negative[j].replace('{POW}','^-')
                    tmp_minus.append(tmp_negative[j])
                tmp[index] = tmp_negative[0] # the first element is always positive
                
        
        # positive terms
        for elmnt in tmp:
            if elmnt != "":
                elmnt = elmnt.replace('{POW}','^-')
                tmp_plus.append(elmnt)

        vector_data.append(tmp_plus)
        vector_data.append(tmp_minus)

        return vector_data

#-------------------------------------------
    def recombine(self,plus_terms,minus_terms):
        # format all monomial terms to mathematica 
        # recombine the plus/minus data into one string
        # and write the result to file

        final_str = ""
        for monomial in plus_terms:
            if (monomial == ''): final_str += '0+'
            else: final_str += monomial + "+"

        for monomial in minus_terms:
            if (monomial == '') : final_str  += "-0"
            else: final_str += "-(" + monomial + ")"
        
        final_str = final_str.replace("+-","-").replace("++","+")

        final_char = final_str[len(final_str)-1]
        if (final_char == '+' or final_char == '-') : final_str = final_str[:len(final_str)-1]

        return final_str
#-------------------------------------------
