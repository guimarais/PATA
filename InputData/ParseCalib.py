#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  20 21:12:55 2019

@author: guimas
"""
import os
import pandas as pd
import numpy as np

def read_calib_file(filename, max_run_index=50000):
    """Reads a PaiBrandao file with runs at various temperatures.
    Parameters
    -----------
    filename: str
        Path and filename with the various runs.
    max_run_index: int
        The maximum expected numebr of runs for each input file.
        Used to build the ID column for each individual run with
        ID = Temp * max_run_index + run_index
    Returns
    -----------
    df: pandas dataframe
        A dataframe with all the data from filename ordered:
        q***: positions
        p***: momentums
        *i**: initial conditions
        *f**: final conditions
        cmx**: Center of mass positions in (x,y,z), x here is an example
        vcmx**: Velocity of the center of mass
        dcol*: Collision parameter
        mang**: Angular momentum of the diatomic
    """
        
    data_line = []
    with open(filename, 'r') as fin:
        header = fin.readline()
        while True:
            try:
                line_initial = fin.readline().split()
                temp = int(line_initial[0][:-1])
                run_index = int(line_initial[1])
                ID = temp*max_run_index + run_index
                
                data_initial = line_initial[3:]
            
                line_final = fin.readline().split()
                data_final = line_final[1:]
            
                data_line.append([ID]+data_initial+data_final)
            
            except: #EOF reached
                break
    
    header = ['ID',
              'qi01', 'qi02', 'qi03', 'qi04', 'qi05', 'qi06', 'qi07', 'qi08', 'qi09', 'qi10', 'qi11', 'qi12',
              'pi01', 'pi02', 'pi03', 'pi04', 'pi05', 'pi06', 'pi07', 'pi08', 'pi09', 'pi10', 'pi11', 'pi12',
              'cmxi1','cmyi1','cmzi1','cmxi2','cmyi2','cmzi2','vcmxi1','vcmyi1','vcmzi1','vcmxi2','vcmyi2','vcmzi2',
              'dcoli','mangxi1','mangyi1','mangzi1','mangxi2','mangyi2','mangzi2',
              'qf01', 'qf02', 'qf03', 'qf04', 'qf05', 'qf06', 'qf07', 'qf08', 'qf09', 'qf10', 'qf11', 'qf12',
              'pf01', 'pf02', 'pf03', 'pf04', 'pf05', 'pf06', 'pf07', 'pf08', 'pf09', 'pf10', 'pf11', 'pf12',
              'cmxf1','cmyf1','cmzf1','cmxf2','cmyf2','cmzf2','vcmxf1','vcmyf1','vcmzf1','vcmxf2','vcmyf2','vcmzf2',
              'dcolf','mangxf1','mangyf1','mangzf1','mangxf2','mangyf2','mangzf2']
    
    df = pd.DataFrame(data = np.array(data_line).astype(float), columns = header)
    df = df.set_index('ID')
    df.index = df.index.astype(int)
    return df
