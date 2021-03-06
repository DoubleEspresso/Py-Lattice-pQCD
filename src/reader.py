#!/usr/bin/python
# -*- python -*-   
# $RCSfile: reader.py,v $

#---------------------------
# module for reading the user
# input for a given diagram.
#---------------------------

import os
import sys

#-------------------------------------------
MATH_RUN = "/Applications/Mathematica.app/Contents/MacOS/MathKernel -script"
#-------------------------------------------
class Reader:
    
    def __init__(self):
        self.file = "diagram.in"
        
#-------------------------------------------
    def read_diagram(self):
            
        indata  = []
        options = {}
        keys    = []
        DELIMIT = '$$'
        COMMENT = '#'
        BEGIN_READ = '::'
        vertices= []
        
        # open file
        for line in open("diagram.in",'rb'):
            indata.append(line.strip().replace("\n",""))

        # construct the dictionary of options found in 
        # diagram.in to make the taylor expanded diagram
        # in mathematica.
        print ''
        print '...Reading diagram.in'            
        print ''
        for line in indata:
            if (len(line)>=1) : 
                if (line[0] == COMMENT): continue
                if (line[:2] == DELIMIT): 
                    print line
                    key = line.split(BEGIN_READ)[0].strip(DELIMIT).replace(" ","")
                    keys.append(key)
                    value = line.split(BEGIN_READ)[1].replace(" ","")
                    options[key] = value

        print ''


        # error checking for now
        if (int(options["TaylorOrder"]) > 1):
            print "ABORT: currently only max of 1st order taylor expansion is implemented with diagram.in."
            exit()

        #------------------------------------------------------------
        # make sure the values for rw and rho are set if integrating
        if (options["Integrate"] == "true"):
            if (options["rw"] == '' or options["rho"] == ''):
                print "ABORT: If integrating, set values for 'rho' and 'rw'."
                exit()

        # setup the expression in mathematica.
        if (options["Diagram"] == ''): 
            print '...Diagram option is empty, using expression in math.in'
        else:
            self.taylor_expand_diagram( options["Diagram"], options )
            

        # return options to the main program
        return options


#-----------------------------------------------------------------------    
    def taylor_expand_diagram(self,expr, options):

        #-------------------------------------------------
        vertices_allowed = ["WQQG","WQQGG","WGGG","WGGGG"]
        props_allowed    = ["WQQ","WGG"]
        ops_allowed      = ["QOP1","QOP2","QOP3","GOP1","GOP2","GOP3"]
        #-------------------------------------------------

        # quick error check
        if (expr.find(".") == -1):
            print "ERROR: Formatting does not look correct for the diagram.in file.  Be sure to include '.' between each vertex."
            exit()
        vertices = expr.split('.')


        # check all vertices will be defined in mathematica.
        for vertex in vertices:
            tmp = vertex.split("[")[0]
            passed = False

            for allowed_v in (vertices_allowed + props_allowed + ops_allowed):
                if (tmp == allowed_v) : passed = True

            if (passed == False) : 
                print "Error: Could not find", vertex, "in allowed vertices."
                exit()
            
        #-----------------------------------------------------
        # ready to setup the expression.                
        # the sum over internal indices
        sum_inds = options["Sum"].replace(" ","").split(",")
        sum_str  = ""
        
        #------------------------------------------------------
        # parse the sum indices and check them for formatting errors
        max_ind = 0

        if ( len(sum_inds) > 1):
            for index in sum_inds:
                if (index.find("ix")==-1):
                    print "Error: index",ix,"has the wrong formatting in diagram.in."
                    exit()
                end = int(index.split("ix")[1])
                if (end > max_ind) : max_ind = end

        options["max_ind"] = max_ind


        #----------------------------------------------------
        # sum over the internal indices
        if len(sum_inds) > 1:
            for index in sum_inds:
                sum_str += "SUM[" + index + "]*"
        else:
            sum_str += "1*"

        #---------------------------------------------------
        # the pre-factor:
        sum_str += options["Factor"] + "*"


        #--------------------------------------------------
        # taylor expansion of each vertex, if necessary
        taylor_expanded = []
        tmp_ind = max_ind + 1
        vert = 0
        for vertex in vertices:
            tmp_inds = ""
            for iter in range(0,int(options["TaylorOrder"])):
                tmp_inds += "ix" + str(tmp_ind) + ","
                tmp_ind += 1
            tmp_inds = tmp_inds[:len(tmp_inds)-1]

            # for more complicated feynman rules, we need a general index replace
            # routine (have to remove tmp indices)
            if (vertex.split("[")[0] == "WGG"  or 
                vertex.split("[")[0] == "WQQ"  or
                vertex.split("[")[0] == "QOP1" or
                vertex.split("[")[0] == "QOP2" ):
                rep1="tmp1->"+"ix"+str(tmp_ind)
                tmp_ind += 1
                rep2="tmp2->"+"ix"+str(tmp_ind) 
                tmp_ind += 1
                rep3="tmp3->"+"ix"+str(tmp_ind)
                tmp_ind += 1
                reps = "{"+rep1+","+rep2+","+rep3+"}"
                vertex = vertex + "/."+reps

            taylor_expanded.append("v"+str(vert) + " = LatticeTaylorExpand"+options["TaylorOrder"]+"[" + vertex + "," + options["ExtMomentum"] + "," + tmp_inds+"]//Expand;")
            vert += 1

        #------------------------------------------------------------
        # make the final string for mathematica to expand
        final_diagram = sum_str
        vert = 0
        for v in taylor_expanded:
            final_diagram += "v" + str(vert) + "."
            vert += 1

        final_diagram = final_diagram[:len(final_diagram)-1] + ';'


        # call mathematica to expand and write the contents to math.in
        # since the taylor expansion in mathematica is a little involved to do
        # for a general diagram (with multiple lattice actions), we change directory
        # and store all taylor expansion codes in a seperate space
        os.chdir("taylor.tmp")
        print "...Success!"
        print "...Running taylor expansion codes"
        print ""
        self.write_to_mathematica(taylor_expanded,final_diagram)
        # run the mathematica script, and port the 
        # taylor expanded result to math.in
        os.popen(MATH_RUN + " diagram.m","r")
        os.popen("mv ../tst.txt ../math.in","r")
        os.chdir("../")

        return 


#--------------------------------------------------------------------------
    def write_to_mathematica(self,taylors,diagram_expr):
        #-------------------------------
        # some output for the user
        vertex_str = ""
        print "...Taylor Expansions"
        print "====================="
        for vert in taylors:
            print "   ", vert
            vertex_str += vert + "\n"
        print "====================="
        print ''

        diagram_expr = "expr=" + diagram_expr

        # write the math codes to a tmp .m executable
        MATH_CODES = ""
        for line in open("lattice_taylor_expand.m",'rb'):
            MATH_CODES += line
            

        MATH_HEADER = """\n

dir=SetDirectory["~/physics/research/perturbativeLattice/form_codes/v1/src/taylor.tmp"]
printDir="~/physics/research/perturbativeLattice/form_codes/v1/src/";

(*printing script*)
PrintToFile[expr_]:= Module[{ans,file}, 
  ans=ToString[expr, FormatType -> InputForm, CharacterEncoding -> "ASCII"];
  Export[printDir<>"tst.txt", ans]];

 """


        MATH_FOOTER = vertex_str + "\n" + diagram_expr + "\n\n" + "PrintToFile[expr];\n" + "Exit[]\n"
        MATH_FILE = open("diagram.m","w")

        MATH_FILE.write(MATH_CODES + "\n" + MATH_HEADER + MATH_FOOTER)
        MATH_FILE.close()
        #------------------------------
        return



