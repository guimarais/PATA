#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 23:29:55 2019

@author: sbrandao
"""
import os
import pandas as pd
import numpy as np

def is_header(line):
    """
    Method that returns true if the first characters in a string are a set of **
    white spaces at the start of the string are strip away before we start the analysis
    """
    #first split the line
    return line.lstrip().startswith("**")
    
def get_trajectory_number(line):
    return line.split()[-1]

def get_input_and_target(line):
    line_parts = line.split()
    line_parts_as_floats = [float(part) for part in line_parts]
    return line_parts_as_floats

def read_input_files(filename):
    #check if filename exists
    if not os.path.isfile(filename):
        raise Exception("Filename does not exist!") # probably not needed...
    #open file
    fh = open(filename,'r')
    state = -1
    new_row = []
    collection = []
    #find keyword 
    for line in fh:
        is_line_header = is_header(line)
        
        if (is_line_header and state == -1):            
            trajectory_number = int(get_trajectory_number(line))
            new_row.append(trajectory_number)
            state = 0
        elif(state >= 0):            
             input_trajectory = get_input_and_target(line)
             new_row = new_row + input_trajectory
             state = state + 1
        
        if(state == 4):
            collection.append(new_row)
            new_row = []
            state = -1

    header = ['traj_id','xi1','yi1','zi1','xi2','yi2','zi2','pxi1','pyi1','pzi1','pxi2','pyi2','pzi2',
              'xi3','yi3','zi3','xi4','yi4','zi4','pxi3','pyi3','pzi3','pxi4','pyi4','pzi4',
              'xf1','yf1','zf1','xf2','yf2','zf2','pxf1','pyf1','pzf1','pxf2','pyf2','pzf2',
              'xf3','yf3','zf3','xf4','yf4','zf4','pxf3','pyf3','pzf3','pxf4','pyf4','pzf4']

    df = pd.DataFrame(data = np.array(collection), columns = header)    
    df = df.set_index('traj_id')
    return df


if __name__ == "__main__":
    qua = read_input_files("../data/h2h2_10K.ver")