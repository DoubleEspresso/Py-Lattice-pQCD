#!/bin/bash

EXE_FILE=$1

if [ -f "form.out.txt" ];
then
    rm form.out.txt
fi

~/physics/utils/form/./tform $EXE_FILE >> form.out.txt
cat form.out.txt | sed '/FORM/,/\*ANSWER/d' | sed '$d' | sed '$d' | tail -n+3