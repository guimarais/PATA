#!/usr/bin/env python3
from DataGenerator import DataGenerator
from Potential import GravPot
import numpy as np


if __name__=="__main__":
    meanPos = [0, 0, 0];
    meanMoment= [0, 0, 0];
    covMoment = [[1., 0, 0], [0, 1., 0], [0, 0, 1.]];
    covPos= [[1., 0, 0], [0, 1., 0], [0, 0, 1.]];
    GravityPot=GravPot();
    data = DataGenerator(10);
    data.GenerateInitialCondition( meanPos, covPos, meanMoment, covMoment);   
    
    data.SetPotential(GravityPot);
    
    data.Propagate(np.linspace(0, 1, 100));
    data.PlotData();
