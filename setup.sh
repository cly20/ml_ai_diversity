#!/bin/sh

if !(conda info --envs | grep -q st_mlApp)
then conda env create -f environment.yml 
fi
conda activate st_mlApp
