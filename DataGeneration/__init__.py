#!/usr/bin/env python3
from DataGenerator import DataGenerator
from Potential import GravPot
import numpy as np


if __name__=="__main__":
    medianPos = [0, 0, 0];
    medianMoment= [0, 0, 0];
    covMoment = [[1., 0, 0], [0, 1., 0], [0, 0, 1.]];
    covPos= [[1., 0, 0], [0, 1., 0], [0, 0, 1.]];
    GravityPot=GravPot();
    data = DataGenerator(10000);
    data.GenerateInitialCondition( medianPos, covPos, medianMoment, covMoment);   
    
    data.SetPotential(GravityPot);
    
    data.Propagate(np.linspace(0, 1, 100));
    #data.PlotData();
