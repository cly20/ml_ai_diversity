#!/bin/sh

if !(conda info --envs | grep -q st_ml_diversity_App)
then conda env create -f environment.yml 
fi
conda activate st_ml_diversity_App
