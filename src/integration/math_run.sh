#!/bin/bash

METHOD=$1

if [ "$METHOD" = "integrate" ] 
  then
    rm math.out
 #   /Applications/Mathematica.app/Contents/MacOS/MathKernel -script 'lattice_integrate.m' >> math.out
    math -script 'lattice_integrate.m' >> math.out
    cat math.out
fi

if [ "$METHOD" = "expand" ]
  then
    rm expand.out
#    /Applications/Mathematica.app/Contents/MacOS/MathKernel -script 'expand_integrand.m' >> expand.out
    math -script 'expand_integrand.m' >> expand.out
    cat expand.out
fi
